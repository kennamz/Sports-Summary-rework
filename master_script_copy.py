import pytesseract  # for the OCR
import re  # for processing the OCR output

import cv2  # for cropping and processing images
from PIL import Image

import numpy as np  # for calculating the movement (pixel difference) of frames
from numpy import sum

from moviepy.editor import *  # for iterating through the frames of the video
import itertools
import pandas as pd  # for reading in inputs, storing data, writing to csvs, etc.
import os  # for saving all files to the right place

import tensorflow as tf  # for classifying the camera angle

saved_model_path = "./model_final"
model = tf.keras.models.load_model(saved_model_path)


##########################################################
# Process the video
##########################################################


def ocr(img):
    img = np.dot(img[..., :3], [0.299, 0.587, 0.114])  # make image grayscale
    img = Image.fromarray(np.uint8(img))

    # crop image
    img = img.crop((left_x, top_y, right_x, bottom_y))
    # img.save(os.path.join(main_path, "imgs/", "crop" + str(random.randint(0,30)) + ".jpg"))

    text = pytesseract.image_to_string(img, config='--psm 7')
    return text


def quarter_and_time(input_str):
    if len(input_str) > 8:  # filter out text that's too short
        # determine quarter
        quarter = -1;
        if input_str.find("st") != -1:
            quarter = 1
        elif input_str.find("nd") != -1:
            quarter = 2
        elif input_str.find("rd") != -1:
            quarter = 3
        elif input_str.find("th") != -1:
            quarter = 4
        elif input_str.find("OT") != -1 or input_str.find("oT") != -1:
            quarter = 5
        else:
            print("error determining quarter", input_str[:-1])
            return

        # format the time left in the quarter
        minute = 0
        second = 0
        fraction = 0
        substr = clock = re.split(" ", input_str)[-1]
        colon = substr.find(":")
        try:
            if colon != -1:
                minute = int(substr[0:colon])
                second = int(substr[colon + 1:colon + 3])
            else:
                decimal = substr.find(".")
                if decimal != -1:
                    second = int(substr[0:decimal])
                    fraction = int(substr[decimal + 1:decimal + 2])
                else:
                    print("error determining time", input_str[:-1])
                    return
        except ValueError:
            print("error determining time", input_str[:-1])
            return

        date = minute * 60 + second + fraction * .1
        return quarter, date

    else:
        print("string input too short", input_str[:-1])
        return None


def determine_angle(img):
    sq_img = cv2.resize(img, dsize=(224, 224))
    expanded = np.expand_dims(sq_img, axis=0)
    prediction_scores = model(expanded)
    predicted_index = np.argmax(prediction_scores)
    return predicted_index


def process_img(img, next_img, audio, timestamp):
    ocr_out = ocr(img)
    quarter_time = quarter_and_time(ocr_out)
    if quarter_time is not None:
        quarter = quarter_time[0]
        time = quarter_time[1]
        diff = difference(img, next_img)
        sound = norm_audio(audio)
        angle = determine_angle(img)

        row = [quarter, time, diff, sound, angle, timestamp]
        return row
    else:
        return None


video = VideoFileClip(os.path.join(main_path, "raw_footage.mp4"))
audio = video.audio
dataframe = [['Quarter', 'Time', 'Difference', 'Sound', 'Angle', 'TimeStamp']]

print("processing video")


def process_video(every_x_frame):
    prev_img = None
    iter = video.iter_frames(with_times=True)

    try:
        while (True):
            t, video_frame = next(itertools.islice(iter, every_x_frame, None))
            audio_frame = audio.get_frame(t)

            if prev_img is not None:
                out = process_img(prev_img, video_frame, audio_frame, t)
                if out is not None:
                    dataframe.append(out)

            prev_img = video_frame
    except StopIteration:
        print("fished iterating")


every_xth_frame = 10
process_video(every_x_frame=every_xth_frame)

data = pd.DataFrame(dataframe[1:], columns=dataframe[0])
data.to_csv(os.path.join(main_path, 'processed_video_data.csv'))

##########################################################
# Incorporate play-by-play data into the video data
##########################################################

# play_by_play = pd.read_csv('processed_pbp.csv', index_col=0);

# data = pd.read_csv('processed_video_data.csv', index_col=0);
data['Event Label'] = len(data) * [0]
data['Event Description'] = len(data) * [""]


def add_description(row):
    q = row['Quarter']
    t = row['Time']

    # dataframe with all events with the same timestamp as row
    df = play_by_play[(play_by_play['period'] == q) & (play_by_play['remaining_seconds_in_period'] == t)]

    description = ""
    for i in range(len(df)):
        description += df['description'].values[i] + ", "

    row['Event Description'] = description

    return row


data.to_csv(os.path.join(main_path, 'video_data_w_events.csv'))

##########################################################
# Select the timestamps to be played in the summary
##########################################################

data = pd.read_csv(os.path.join(main_path, 'video_data_w_events.csv'), index_col=0)
events = data[data['Event Description'].notna()].drop_duplicates(subset=['Quarter', 'Time'])

index_minus = 10
index_plus = 10
min_length = 3

clips = []

for index in events.index:
    start = None
    end = None

    for i in range(index - index_minus, index + index_plus):
        if (i < index) and (start is None) and (data.iloc[i]['Angle'] == 1):
            start = data.iloc[i]['TimeStamp']
        if (i == index) and (start is None):
            start = data.iloc[i]['TimeStamp']
        elif (i < len(data)) and (end is None) and (data.iloc[i]['Angle'] != 1):
            end = data.iloc[i - 1]['TimeStamp']
        if (i == index + index_plus - 1) and (end is None):
            if i < len(data):
                end = data.iloc[i]['TimeStamp']
            else:
                end = data.iloc[len(data) - 1]['TimeStamp']
    if end - start > min_length:
        label = data.iloc[index]['Event Label']
        description = data.iloc[index]['Event Description']
        clips.append((start, end, label, description))

clips_df = pd.DataFrame(clips, columns=['Start', 'End', 'Label', 'Description'])
clips_df.to_csv(os.path.join(main_path, 'clips.csv'))
