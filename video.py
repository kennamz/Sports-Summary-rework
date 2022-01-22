import re
from enum import Enum
import cv2
import tensorflow as tf
import numpy as np
from PIL import Image
from pytesseract import pytesseract

import event


class CameraAngle(Enum):
    PROFILE = 0,
    CLOSE_UP = 1


class Frame:
    def __init__(self, angle, timestamp, game_time):
        self.angle = angle
        self.timestamp = timestamp
        self.game_time = game_time


class VideoProcessing:
    ML_MODEL_PATH = "./model_final"

    def __init__(self, game):
        self.youtube_link = game.youtube_link
        self.file_name = 'LongOvertimeClip.mp4'

        self.game_events = game.events
        if self.game_events is None:
            print("no game events found!")

        self.game_clock = game.clock
        print(type(self.game_clock), type(game.clock))

        self.model = tf.keras.models.load_model(self.ML_MODEL_PATH)

        self.frames = []

    def process_video(self):
        capture = cv2.VideoCapture(self.file_name)

        while True:
            grabbed, frame = capture.read()
            if not grabbed:
                break

            angle = self.determine_angle(frame)
            timestamp = capture.get(cv2.CAP_PROP_POS_MSEC)
            game_time = self.determine_game_time(frame)

            self.frames.append(Frame(angle, timestamp, game_time))

    def determine_angle(self, img):
        sq_img = cv2.resize(img, dsize=(224, 224))
        expanded = np.expand_dims(sq_img, axis=0)
        prediction_scores = self.model(expanded)
        predicted_index = np.argmax(prediction_scores)

        return CameraAngle.CLOSE_UP if predicted_index == 0 else CameraAngle.PROFILE

    def determine_game_time(self, img):
        img = Image.fromarray(np.uint8(img))

        print(type(self.game_clock))
        img = img.crop((self.game_clock.left_x,
                        self.game_clock.top_y,
                        self.game_clock.right_x,
                        self.game_clock.bottom_y))

        text = pytesseract.image_to_string(img, config='--psm 7')
        return parse_game_time_from_ocr(text)


def parse_game_time_from_ocr(input_str):
    if len(input_str) > 8:  # filter out text that's too short
        # determine quarter
        quarter = -1
        if input_str.find("st") != -1:
            quarter = event.Quarter.FIRST
        elif input_str.find("nd") != -1:
            quarter = event.Quarter.SECOND
        elif input_str.find("rd") != -1:
            quarter = event.Quarter.THIRD
        elif input_str.find("th") != -1:
            quarter = event.Quarter.FOURTH
        elif input_str.find("OT") != -1 or input_str.find("oT") != -1:
            quarter = event.Quarter.OVERTIME_1
        else:
            print("error determining quarter", input_str[:-1])
            return

        try:
            time = re.split(r" ", input_str)[-1]
            time = re.sub(r"[^0-9:]", "", time)  # strip all chars not relevant to time

        except ValueError:
            print("error determining time", input_str[:-1])
            return

        time = event.GameTime(quarter, time)
        return time

    else:
        print("string input too short", input_str[:-1])
        return None
