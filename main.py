import numpy
import vlc

from screen import Screen
from summarizer import Summarizer
from video import *

import pandas as pd
import jsons
import json
import tkinter as tk


def read_inputs():
    inputs = pd.read_csv('input_final.csv').iloc[0].to_list()
    for index in range(len(inputs)):
        if isinstance(inputs[index], numpy.int64):
            inputs[index] = int(inputs[index])
    return Game(inputs)


def create_game(create_new_game, file_name):
    if create_new_game:
        print("Creating new game")

        game = read_inputs()
        game.process_events()

        json_out = jsons.dump(game)
        json_object = json.dumps(json_out, indent=2)
        with open(file_name, 'w') as f:
            print(json_object, file=f)

            f.close()
    else:
        print("Reading game from", file_name)

        with open(file_name, 'r') as f:
            json_object = json.load(f)
            game = jsons.load(json_object, Game)

            f.close()
    return game


def create_video_data(process_new_video, file_name):
    if process_new_video:
        video = VideoProcessing(final_game)
        video.process_video(file_name)
    else:
        video = VideoProcessing(file_name)
    return video


if __name__ == '__main__':
    final_game = create_game(True, "game.json")

    # print(type(game.inputs), type(game.date), type(game.home_team), type(game.clock), type(game.events))
    # for event in game.events:
    #     print(type(event))

    final_video = create_video_data(False, "long_video.data")

    print("Beginning summarization")

    summarizer = Summarizer(final_game, final_video)
    summarizer.create_summary()

    for item in summarizer.summary:
        print(item)

    root = tk.Tk()
    player = Screen(root, 'raw_footage.mp4')
    player.play_summary(summarizer.summary)

    root.mainloop()  # to keep the GUI open

