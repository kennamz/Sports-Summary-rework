import sys

import numpy

from game import *
from screen import *
from summarizer import Summarizer
from video import *

import pandas as pd
import jsons
import json


def read_inputs():
    inputs = pd.read_csv('input_final.csv').iloc[0].to_list()
    for index in range(len(inputs)):
        if isinstance(inputs[index], numpy.int64):
            inputs[index] = int(inputs[index])
    return Game(inputs)


if __name__ == '__main__':
    create_new_game = True
    file_name = "game.json"

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

    # print(type(game.inputs), type(game.date), type(game.home_team), type(game.clock), type(game.events))
    # for event in game.events:
    #     print(type(event))

    process_new_video = False
    file_name = "video.data"

    if process_new_video:
        video = VideoProcessing(game)
        video.process_video()
    else:
        video = VideoProcessing(file_name)

    print("Beginning summarization")

    summarizer = Summarizer(game, video)
    summarizer.create_summary()

    # root = tk.Tk()
    # player = Screen(root)
    #
    # root.mainloop()  # to keep the GUI open
