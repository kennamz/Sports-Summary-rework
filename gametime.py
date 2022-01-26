import event
from datetime import timedelta
import re


class GameTime:
    def __init__(self, quarter, time_left):
        if quarter is None or time_left is None:
            print("Warning: None input in GameTime")
        if not isinstance(quarter, event.Quarter):
            print("Warning: quarter input is not of type event.Quarter")

        self.quarter = quarter

        if isinstance(time_left, str):
            self.time_left = parse_timedelta_from_str(time_left)
        elif not isinstance(time_left, timedelta):
            print("Warning: time_left input is not of type timedelta or str")
            self.time_left = time_left
        else:
            self.time_left = time_left

    def __str__(self):
        return "Quarter: " + str(self.quarter) + ", Time Remaining: " + str(self.time_left)


def parse_timedelta_from_str(time_left_str):
    try:
        colon_split = re.split(r":", time_left_str)
        minutes = int(colon_split[0])

        period_split = re.split(r"\.", colon_split[1])
        seconds = int(period_split[0])

        milliseconds = 0
        if len(period_split) > 1:
            milliseconds = int(period_split[1]) * 100

        delta = timedelta(minutes=minutes,
                          seconds=seconds,
                          milliseconds=milliseconds)

        return delta
    except:
        print("Error in parse_timedelta_from_str()")
        return None
