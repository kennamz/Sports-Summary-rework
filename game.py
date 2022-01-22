import datetime
import os

from event import *
from scrape import Scraper


class Date:
    def __init__(self, month, day, year):
        self.month_of_game = month
        self.num_month = datetime.datetime.strptime(self.month_of_game, "%B").month
        self.day_of_game = day
        self.year_of_game = year


class GameClock:
    def __init__(self, top_y, left_x, bottom_y, right_x):
        self.top_y = top_y
        self.left_x = left_x
        self.bottom_y = bottom_y
        self.right_x = right_x


class Game:
    def __init__(self, inputs):
        # self.youtube_link = inputs[0]
        self.youtube_link = "https://youtu.be/60N0x6dgFxs"

        self.inputs = inputs

        self.date = Date(self.inputs[1], int(self.inputs[2]), int(self.inputs[3]))

        home_team_str = self.inputs[4]
        away_team_str = self.inputs[5]
        self.home_team = TEAM_NAME_TO_TEAM[home_team_str.upper()]
        self.away_team = TEAM_NAME_TO_TEAM[away_team_str.upper()]

        self.main_path = os.path.join("../watch/", str(self.date.year_of_game) + "_" +
                                      self.date.month_of_game + "_" + str(self.date.day_of_game) + "_" +
                                      home_team_str + "_" + away_team_str)

        self.clock = GameClock(self.inputs[6], self.inputs[7], self.inputs[8], self.inputs[9])

        self.events = None

    def process_events(self):
        scraper = Scraper(self)
        self.events = scraper.scrape_all()
