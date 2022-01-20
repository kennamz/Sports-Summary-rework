from game import *
from screen import *
from video import *

import pandas as pd


def read_inputs():
    inputs = pd.read_csv('input_final.csv').iloc[0].to_list()
    return Game(inputs)


if __name__ == '__main__':
    game = read_inputs()
    game.process_events()

    video = VideoProcessing(game)
    video.process_video()

    root = tk.Tk()
    player = Screen(root)

    root.mainloop()  # to keep the GUI open

