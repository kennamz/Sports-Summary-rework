from event import Event
from video import CameraAngle


class SummaryItem:
    def __init__(self, events, begin_time, end_time):
        if isinstance(events, list):
            self.events = events
        else:
            self.events = [events]

        self.begin_time = begin_time
        self.end_time = end_time

    def __str__(self):
        # event_type = str(self.events[0].event_type)
        begin = str(round(self.begin_time, 1))
        end = str(round(self.end_time, 1))
        length = str(round(self.clip_length(), 1))
        return "Summary item with " + str(len(self.events)) + " events, from " + \
               begin + " s to " + end + " s, length " + length + " s"

    def add_event(self, new_event):
        if isinstance(self.events, list):
            self.events.append(new_event)
        else:
            self.events = [self.events, new_event]

    def clip_length(self):
        return self.end_time - self.begin_time


class Summarizer:
    def __init__(self, game, video):
        if game.events is None or len(game.events) == 0:
            print("no game events found!")
        if video.frames is None or len(video.frames) == 0:
            print("no video frame data found!")

        self.events = game.events
        self.frames = video.frames

        self.summary = []

    def create_summary(self):
        compiled_events = Event.compile_events(self.events)

        for event in compiled_events:

            timestamps = find_timestamp(event[0].time, self.frames)
            if timestamps is None:
                # print("No matching timestamp found for event", event)
                continue
            matching_frames, indexes = timestamps

            begin_index = indexes[0]
            end_index = indexes[1]

            begin_time = find_prev_close_up(begin_index, self.frames)
            end_time = find_next_close_up(end_index, self.frames)
            if begin_time is None or end_time is None:
                continue

            summary_item = SummaryItem(event, begin_time/1000, end_time/1000)
            self.summary.append(summary_item)
        self.compile_summary()

    def compile_summary(self):
        def summary_item_begin_time(item):
            return item.begin_time

        self.summary.sort(key=summary_item_begin_time)

        for i in range(len(self.summary)):
            for j in range(i+1, len(self.summary)):
                if self.summary[j].begin_time == self.summary[i].begin_time:
                    continue


def find_prev_close_up(begin_index, frames):
    prev_i = begin_index
    initial_timestamp = frames[begin_index].timestamp
    for i in range(len(frames[:begin_index]) - 1, -1, -1):  # iterate backwards
        frame = frames[i]

        difference = abs(frame.timestamp - initial_timestamp)
        max_prev_time_dif = 4 * 1000
        if difference > max_prev_time_dif:
            print("over max difference", difference)
            return frames[prev_i].timestamp

        if frame.angle == CameraAngle.CLOSE_UP:
            # print("prev_i", prev_i, begin_index)
            return frames[prev_i].timestamp

        prev_i = i


def find_next_close_up(end_index, frames):
    ending_frames = frames[end_index:]
    prev_i = 0
    initial_timestamp = frames[end_index].timestamp
    for i in range(len(ending_frames)):
        frame = ending_frames[i]

        difference = abs(frame.timestamp - initial_timestamp)
        max_prev_time_dif = 4 * 1000
        if difference > max_prev_time_dif:
            print("over max difference find_next_close_up", difference)
            return frames[prev_i+end_index].timestamp

        if frame.angle == CameraAngle.CLOSE_UP:
            return frames[prev_i+end_index].timestamp

        prev_i = i


def find_timestamp(game_time, frames):
    matches = []
    begin_index = None
    end_index = None
    last_was_match = False

    for index in range(len(frames)):
        frame = frames[index]
        quarter_matches = frame.game_time.quarter == game_time.quarter
        time_matches = frame.game_time.time_left == game_time.time_left

        if quarter_matches and time_matches:
            if not last_was_match:
                begin_index = index
            last_was_match = True
            matches.append(frame)
        else:
            if last_was_match:
                end_index = index - 1
            last_was_match = False
            continue

    if len(matches) == 0 or begin_index is None or end_index is None:
        return None
    else:
        return matches, (begin_index, end_index)
