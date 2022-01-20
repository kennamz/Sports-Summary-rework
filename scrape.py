import requests
import re
from bs4 import BeautifulSoup

from event import *


class Scraper:
    BASE_URL = 'https://www.basketball-reference.com'

    @staticmethod
    def full_name_from_ref(ref_tag):
        return ""

    def __init__(self, game):
        self.game = game
        self.play_by_play_url, self.shot_chart_url = self.create_urls()
        self.events = None

    def create_urls(self):
        # source: https://github.com/jaebradley/basketball_reference_web_scraper
        def add_0_if_needed(s):
            s = str(s)
            return "0" + s if len(s) == 1 else s

        year = str(self.game.date.year_of_game)
        month = str(add_0_if_needed(self.game.date.num_month))
        day = str(add_0_if_needed(self.game.date.day_of_game))
        team_abbr = str(TEAM_TO_TEAM_ABBREVIATIONS[self.game.home_team])

        pbp_url = self.BASE_URL + "/boxscores/pbp/" + year + month + day + "0" + team_abbr + ".html"
        shot_chart_url = self.BASE_URL + "/boxscores/shot-chart/" + year + month + day + "0" + team_abbr + ".html"

        return pbp_url, shot_chart_url

    def scrape_all(self):
        # testing_pbp_urls = ["https://www.basketball-reference.com/boxscores/pbp/202201140SAC.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/202110300WAS.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/202110300IND.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/202110300DET.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/201305050OKC.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/201211120TOR.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/201203250ATL.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/200502220HOU.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/201002200CHI.html",
        #                     "https://www.basketball-reference.com/boxscores/pbp/200612160NYK.html"]
        #
        # testing_position_urls = ["https://www.basketball-reference.com/boxscores/shot-chart/202201140SAC.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/202110300WAS.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/202110300IND.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/202110300DET.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/201305050OKC.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/201211120TOR.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/201203250ATL.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/200502220HOU.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/201002200CHI.html",
        #                          "https://www.basketball-reference.com/boxscores/shot-chart/200612160NYK.html"]

        self.shot_chart_url = "https://www.basketball-reference.com/boxscores/shot-chart/201205300MIA.html"
        self.play_by_play_url = "https://www.basketball-reference.com/boxscores/pbp/201205300MIA.html"

        self.scrape_pbp()
        self.scrape_shot_positions()
        print("finished scrape_all()")
        return self.events

        # for index in range(len(testing_pbp_urls)):
        #     self.play_by_play_url = testing_pbp_urls[index]
        #     self.shot_chart_url = testing_position_urls[index]
        #
        #     print("----", index, "----")
        #
        #     self.scrape_pbp()
        #     self.scrape_shot_positions()

    def scrape_pbp(self):
        html = requests.get(self.play_by_play_url).text
        parsed_html = BeautifulSoup(html, features="html.parser")

        table = parsed_html.find('table', id="pbp")
        if table is None:
            raise Exception("No play by play table in url")
        rows = table.find_all("tr")

        events = []
        current_quarter = Quarter.FIRST
        for row in rows:
            if row.get('id') is not None:
                current_quarter = parse_current_quarter(row)
                continue
            elif row.get('class') is not None and "thead" in row.get('class'):
                continue

            time_remaining = row.td.text
            time = GameTime(current_quarter, time_remaining)
            relevant_team = parse_relevant_team(row, self.game.home_team, self.game.away_team)
            score = parse_score(row)
            description = parse_description(row)
            event_type = determine_event_type(row)

            event = create_event(row, time, relevant_team, score, description, event_type)
            events.append(event)
        self.events = events

    def scrape_shot_positions(self):
        html = requests.get(self.shot_chart_url).text
        parsed_html = BeautifulSoup(html, features="html.parser")

        for tag in parsed_html.body.find_all('div', attrs={'class': 'tooltip'}):
            tip_text = tag['tip']
            classes = tag['class']
            style_text = tag['style']

            time = parse_time(tip_text, classes)
            make = parse_make_from_classes(classes)
            points = parse_points(tip_text)
            player = parse_player(classes)
            position = parse_position(style_text)

            self.add_position_to_shot(time, make, points, player, position)

    def add_position_to_shot(self, time, make, points, player, position):
        for index in range(len(self.events)):
            event = self.events[index]
            if event.event_type == points:
                if event.make == make:
                    if event.time.quarter == time.quarter and event.time.time_left == time.time_left:
                        if event.player.ref_tag == player.ref_tag:
                            self.events[index].position = position
                            return
        print("no matching event found")


######################################
# scrape_pbp() helpers
######################################

def parse_current_quarter(row):
    row_id = row['id']
    if row_id == "q1":
        return Quarter.FIRST
    elif row_id == "q2":
        return Quarter.SECOND
    elif row_id == "q3":
        return Quarter.THIRD
    elif row_id == "q4":
        return Quarter.FOURTH
    elif row_id == "q5":
        return Quarter.OVERTIME_1
    elif row_id == "q6":
        return Quarter.OVERTIME_2
    elif row_id == "q7":
        return Quarter.OVERTIME_3
    elif row_id == "q8":
        return Quarter.OVERTIME_4
    elif row_id == "q9":
        return Quarter.OVERTIME_5
    elif row_id == "q10":
        return Quarter.OVERTIME_6


def determine_event_type(row):
    if row.td.next_sibling.next_sibling.get('colspan') is not None:
        third_sib_txt = row.td.next_sibling.next_sibling.text.lower()
        if "jump" in third_sib_txt:
            return EventType.JUMP_BALL
        elif "end" in third_sib_txt or "start" in third_sib_txt:
            return EventType.QUARTER_START_END

    away_team_txt = row.td.next_sibling.next_sibling.text.lower()
    home_team_txt = row.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.lower()
    if away_team_txt.isspace() and home_team_txt.isspace():
        print("error determining relevant_text")
    relevant_text = away_team_txt if not away_team_txt.isspace() else home_team_txt

    if "free throw" in relevant_text:
        return EventType.FREE_THROW
    elif "2-pt" in relevant_text:
        return EventType.TWO_PTR
    elif "3-pt" in relevant_text:
        return EventType.THREE_PTR
    elif "rebound" in relevant_text:
        return EventType.REBOUND
    elif "turnover" in relevant_text:
        return EventType.TURNOVER
    elif "foul" in relevant_text:
        return EventType.FOUL
    elif "violation" in relevant_text:
        return EventType.VIOLATION
    elif "timeout" in relevant_text:
        return EventType.TIMEOUT
    elif "enters the game" in relevant_text:
        return EventType.ENTERS_THE_GAME
    elif "replay" in relevant_text:
        return EventType.INSTANT_REPLAY
    elif "ejected" in relevant_text:
        return EventType.EJECTION
    else:
        print("unable to determine event type: ", relevant_text)
        return EventType.OTHER


def parse_relevant_team(row, home_team, away_team):
    if row.td.next_sibling.next_sibling.get('colspan') is not None:  # jump ball or start/end
        return None

    away_team_txt = row.td.next_sibling.next_sibling.text.lower()
    home_team_txt = row.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.lower()
    if away_team_txt.isspace() == home_team_txt.isspace():
        print("error determining relevant_text")
    return home_team if not home_team_txt.isspace else away_team


def parse_score(row):
    if row.td.next_sibling.next_sibling.get('colspan') is not None:  # jump ball or start/end
        return None

    score_text = row.td.next_sibling.next_sibling.next_sibling.next_sibling.text
    scores = re.split(r"-", score_text)

    return Score(scores[1], scores[0])


def parse_description(row):
    if row.td.next_sibling.next_sibling.get('colspan') is not None:
        third_sib_txt = row.td.next_sibling.next_sibling.text
        return third_sib_txt

    away_team_txt = row.td.next_sibling.next_sibling.text
    home_team_txt = row.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    if away_team_txt.isspace() and home_team_txt.isspace():
        print("error determining relevant_text")
    relevant_text = away_team_txt if not away_team_txt.isspace() else home_team_txt
    return relevant_text


def create_event(row, time, relevant_team, score, description, event_type):
    if event_type is EventType.QUARTER_START_END:
        return QuarterStartOrEnd(time, relevant_team, score, description, event_type)
    elif event_type is EventType.FREE_THROW:
        return create_free_throw(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.TWO_PTR or event_type is EventType.THREE_PTR:
        return create_shot(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.REBOUND:
        return create_rebound(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.FOUL:
        return create_foul(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.TURNOVER:
        return create_turnover(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.VIOLATION:
        return create_violation(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.TIMEOUT:
        return create_timeout(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.ENTERS_THE_GAME:
        return create_enters_the_game(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.JUMP_BALL:
        return create_jump_ball(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.INSTANT_REPLAY:
        return create_replay(row, time, relevant_team, score, description, event_type)
    elif event_type is EventType.EJECTION:
        return create_ejection(row, time, relevant_team, score, description, event_type)
    else:
        print("creating generic event for", event_type)
        return Event(time, relevant_team, score, description, event_type)


def player_from_link(a_tag):
    if a_tag is None:
        return None

    href = a_tag['href']
    sections = re.split(r"/", href)

    player_page = sections[-1]
    sections = re.split(r"\.", player_page)
    player_tag = sections[0]
    full_name = Scraper.full_name_from_ref(player_tag)

    return Player(player_tag, full_name)


def parse_make_from_description(description):
    if 'makes' in description.lower():
        return Make.MAKE
    elif 'misses' in description.lower():
        return Make.MISS
    else:
        print("error determining make or miss")
        return None


def create_free_throw(row, time, relevant_team, score, description, event_type):
    player = player_from_link(row.a)
    make = parse_make_from_description(description)

    numbers = re.findall(r'[0-9]+', description)
    shot_number = numbers[0] if not len(numbers) == 0 else None
    total = numbers[1] if not len(numbers) == 0 else None

    return FreeThrow(time, relevant_team, score, description, event_type,
                     player, make, shot_number, total)


def parse_made_shot(description):
    description = description.lower()
    if "misses" in description:
        return Make.MISS
    elif "makes" in description:
        return Make.MAKE
    else:
        print("could not determine shot make", description)


def parse_block(row):
    if "block by" in row.text:
        return player_from_link(row.find_next('a').find_next('a'))
    else:
        return None


def parse_assist(row):
    if "assist by" in row.text:
        return player_from_link(row.find_next('a').find_next('a'))
    else:
        return None


def parse_distance(description):
    if "at rim" in description.lower():
        return 0

    before_ft = re.search(r"^.*(?=\sft)", description)[0]
    words = re.split(r"\s", before_ft)

    return int(words[-1])


def create_shot(row, time, relevant_team, score, description, event_type):
    player = player_from_link(row.a)

    make = parse_made_shot(description)
    blocked_by = parse_block(row)
    assist_by = parse_assist(row)
    distance = parse_distance(description)

    position = None

    return FieldGoal(time, relevant_team, score, description, event_type,
                     player, make, blocked_by, assist_by, distance, position)


def create_rebound(row, time, relevant_team, score, description, event_type):
    player = player_from_link(row.a) if row.a is not None else None
    rebound_type = ReboundType.DEFENSIVE if "defensive" in description.lower() else ReboundType.OFFENSIVE

    return Rebound(time, relevant_team, score, description, event_type,
                   player, rebound_type)


def parse_foul_type(description):
    description = description.lower()
    if "shooting" in description:
        return FoulType.SHOOTING
    elif "loose ball" in description:
        return FoulType.LOOSE_BALL
    elif "personal" in description:
        return FoulType.PERSONAL
    elif "def 3 sec" in description:
        return FoulType.DEF_THREE_SECOND
    elif "flagrant" in description:
        return FoulType.FLAGRANT
    elif "offensive" in description:
        return FoulType.OFFENSIVE
    elif "blocking" in description:
        return FoulType.BLOCKING
    elif "charging" in description:
        return FoulType.CHARGING
    elif "defensive" in description:
        return FoulType.DEFENSIVE
    elif "double" in description:
        return FoulType.DOUBLE
    elif "illegal screen" in description:
        return FoulType.ILLEGAL_SCREEN
    elif "intentional" in description:
        return FoulType.INTENTIONAL
    elif "punching" in description:
        return FoulType.PUNCHING
    elif "reach in" in description:
        return FoulType.REACH_IN
    elif "technical" in description:
        return FoulType.TECHNICAL
    elif "take" in description:
        return FoulType.TAKE
    elif "away from play" in description:
        return FoulType.AWAY_FROM_PLAY
    elif "clear path" in description:
        return FoulType.CLEAR_PATH
    else:
        print("unknown foul type", description)
        return FoulType.OTHER


def create_foul(row, time, relevant_team, score, description, event_type):
    player = player_from_link(row.a) if row.a is not None else None

    drawn_by = None if row.a is None or row.a.next_sibling is None else player_from_link(
        row.a.next_sibling.next_sibling)

    foul_type = parse_foul_type(description)

    return Foul(time, relevant_team, score, description, event_type,
                player, drawn_by, foul_type)


def parse_turnover_type(description):
    description = description.lower()
    if "bad pass" in description:
        return TurnoverType.BAD_PASS
    elif "offensive foul" in description:
        return TurnoverType.OFFENSIVE_FOUL
    elif "traveling" in description:
        return TurnoverType.TRAVELING
    elif "shot clock" in description:
        return TurnoverType.SHOT_CLOCK
    elif "out of bounds lost ball" in description:
        return TurnoverType.OUT_OF_BOUNDS_LOST_BALL
    elif "step out of bounds" in description:
        return TurnoverType.STEP_OUT_OF_BOUNDS
    elif "lost ball" in description:
        return TurnoverType.LOST_BALL
    elif "3 sec" in description:
        return TurnoverType.THREE_SECOND
    elif "5 sec" in description:
        return TurnoverType.FIVE_SECOND
    elif "8 sec" in description:
        return TurnoverType.EIGHT_SECOND
    elif "back court" in description:
        return TurnoverType.BACK_COURT
    elif "discontinued dribble" in description:
        return TurnoverType.DISCONTINUED_DRIBBLE
    elif "inbound" in description:
        return TurnoverType.INBOUND
    elif "offensive goaltending" in description:
        return TurnoverType.OFFENSIVE_GOALTENDING
    else:
        print("could not determine turnover type", description)
        return TurnoverType.OTHER


def parse_steal(row):
    if "steal by" not in row.text:
        return None
    if row.a.next_sibling.next_sibling is not None:
        return player_from_link(row.a.next_sibling.next_sibling)


def create_turnover(row, time, relevant_team, score, description, event_type):
    player = player_from_link(row.a)
    steal_by = parse_steal(row)
    turnover_type = parse_turnover_type(description)
    return Turnover(time, relevant_team, score, description, event_type,
                    player, steal_by, turnover_type)


def parse_violation_type(description):
    description = description.lower()
    if "kicked ball" in description:
        return ViolationType.KICKED_BALL
    elif "delay of game" in description:
        return ViolationType.DELAY_OF_GAME
    elif "def goaltending" in description:
        return ViolationType.DEFENSIVE_GOALTENDING
    else:
        print("could not determine violation type", description)
        return ViolationType.OTHER


def create_violation(row, time, relevant_team, score, description, event_type):
    player = player_from_link(row.a)
    violation_type = parse_violation_type(description)

    return Violation(time, relevant_team, score, description, event_type,
                     player, violation_type)


def parse_timeout_type(description):
    description = description.lower()
    if "20 second" in description:
        return TimeoutType.TWENTY_SECOND
    elif "full" in description:
        return TimeoutType.FULL
    elif "official" in description:
        return TimeoutType.OFFICIAL
    else:
        print("could not determine timeout type", description)
        return TimeoutType.OTHER


def create_timeout(row, time, relevant_team, score, description, event_type):
    timeout_type = parse_timeout_type(description)
    return Timeout(time, relevant_team, score, description, event_type,
                   timeout_type)


def create_enters_the_game(row, time, relevant_team, score, description, event_type):
    entering_player = player_from_link(row.a)
    subbed_player = player_from_link(row.a.next_sibling.next_sibling)

    return EntersTheGame(time, relevant_team, score, description, event_type,
                         entering_player, subbed_player)


def parse_replay_type(description):
    description = description.lower()
    if "challenge" in description:
        return InstantReplayType.CHALLENGE
    elif "request" in description:
        return InstantReplayType.REQUEST
    else:
        print("could not determine replay type", description)
        return InstantReplayType.REQUEST


def parse_replay_outcome(description):
    description = description.lower()
    if "stands" in description:
        return InstantReplayOutcome.STANDS
    else:
        return InstantReplayOutcome.OVERTURNED


def create_replay(row, time, relevant_team, score, description, event_type):
    replay_type = parse_replay_type(description)
    outcome = parse_replay_outcome(description)

    return InstantReplay(time, relevant_team, score, description, event_type,
                         replay_type, outcome)


def create_jump_ball(row, time, relevant_team, score, description, event_type):
    away_player = player_from_link(row.find_next('a'))
    home_player = player_from_link(row.find_next('a').find_next('a'))

    if "gains possession" in description:
        gains_possession = row.find_next('a').find_next('a').find_next('a')
    else:
        gains_possession = None

    return JumpBall(time, relevant_team, score, description, event_type,
                    home_player, away_player, gains_possession)


def create_ejection(row, time, relevant_team, score, description, event_type):
    player = player_from_link(row.a)

    return Ejection(time, relevant_team, score, description, event_type,
                    player)


######################################
# scrape_shot_positions() helpers
######################################

def parse_time(tip_text, classes):
    quarter = None
    if 'q-1' in classes:
        quarter = Quarter.FIRST
    elif 'q-2' in classes:
        quarter = Quarter.SECOND
    elif 'q-3' in classes:
        quarter = Quarter.THIRD
    elif 'q-4' in classes:
        quarter = Quarter.FOURTH
    elif 'q-5' in classes:
        quarter = Quarter.OVERTIME_1
    elif 'q-6' in classes:
        quarter = Quarter.OVERTIME_2
    elif 'q-7' in classes:
        quarter = Quarter.OVERTIME_3
    elif 'q-8' in classes:
        quarter = Quarter.OVERTIME_4
    elif 'q-9' in classes:
        quarter = Quarter.OVERTIME_5
    elif 'q-10' in classes:
        quarter = Quarter.OVERTIME_6

    time = re.split(r"\s", tip_text)[2]

    return GameTime(quarter, time)


def parse_make_from_classes(classes):
    make = None
    if 'make' in classes:
        make = Make.MAKE
    elif 'miss' in classes:
        make = Make.MISS

    return make


def parse_points(tip_text):
    points = None
    if '2-pointer' in tip_text:
        points = EventType.TWO_PTR
    elif '3-pointer' in tip_text:
        points = EventType.THREE_PTR

    return points


def parse_player(classes):
    for class_instance in classes:
        if 'p-' in class_instance:
            sections = re.split(r"-", class_instance)
            player_tag = sections[-1]
            return Player(player_tag, Scraper.full_name_from_ref(player_tag))

    return None


def parse_position(style_text):
    top = None
    left = None

    positions = re.split(r";", style_text)

    top_raw = positions[0]
    top_raw = re.split(r":", top_raw)
    top_raw = re.search(r"^.*(?=px)", top_raw[1])
    if top_raw is not None:
        top = top_raw[0]

    left_raw = positions[1]
    left_raw = re.split(r":", left_raw)
    left_raw = re.search(r"^.*(?=px)", left_raw[1])
    if left_raw is not None:
        left = left_raw[0]

    return Position(top, left)
