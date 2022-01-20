import cv2


class VideoProcessing:
    def __init__(self, game):
        self.youtube_link = game.youtube_link
        self.file_name = 'LongOvertimeClip.mp4'

        self.game_events = game.events
        if self.game_events is None:
            print("no game events found!")

    def process_video(self):
        capture = cv2.VideoCapture(self.file_name)
        while True:
            grabbed, frame = capture.read()
            if not grabbed:
                break
