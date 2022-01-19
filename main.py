from game import *

import pandas as pd


def read_inputs():
    inputs = pd.read_csv('input_final.csv').iloc[0].to_list()
    return Game(inputs)


if __name__ == '__main__':
    game = read_inputs()
    game.process_events()
