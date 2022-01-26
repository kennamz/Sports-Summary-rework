class SummaryItem:
    def __int__(self, event, begin_time, end_time):
        self.event = event
        self.begin_time = begin_time
        self.end_time = end_time


class Summarizer:
    def __init__(self, game, video):
        if game.events is None or len(game.events) == 0:
            print("no game events found!")
        if video.frames is None or len(video.frames) == 0:
            print("no video frame data found!")

        self.events = game.events
        self.frames = video.frames

    def create_summary(self):
        summary = []
        for event in self.events:
            timestamps = find_timestamp(event.time, self.frames)
            if timestamps is None:
                print("No matching timestamp found for event", event)
                continue
            matching_frames, indexes = timestamps
            begin_index = indexes[0]
            end_index = indexes[1]


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

    if len(matches) == 0:
        return None
    else:
        return matches, (begin_index, end_index)


