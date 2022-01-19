from enum import Enum, auto


class Team(Enum):  # source: https://github.com/jaebradley/basketball_reference_web_scraper
    ATLANTA_HAWKS = "ATLANTA HAWKS"
    BOSTON_CELTICS = "BOSTON CELTICS"
    BROOKLYN_NETS = "BROOKLYN NETS"
    CHARLOTTE_HORNETS = "CHARLOTTE HORNETS"
    CHICAGO_BULLS = "CHICAGO BULLS"
    CLEVELAND_CAVALIERS = "CLEVELAND CAVALIERS"
    DALLAS_MAVERICKS = "DALLAS MAVERICKS"
    DENVER_NUGGETS = "DENVER NUGGETS"
    DETROIT_PISTONS = "DETROIT PISTONS"
    GOLDEN_STATE_WARRIORS = "GOLDEN STATE WARRIORS"
    HOUSTON_ROCKETS = "HOUSTON ROCKETS"
    INDIANA_PACERS = "INDIANA PACERS"
    LOS_ANGELES_CLIPPERS = "LOS ANGELES CLIPPERS"
    LOS_ANGELES_LAKERS = "LOS ANGELES LAKERS"
    MEMPHIS_GRIZZLIES = "MEMPHIS GRIZZLIES"
    MIAMI_HEAT = "MIAMI HEAT"
    MILWAUKEE_BUCKS = "MILWAUKEE BUCKS"
    MINNESOTA_TIMBERWOLVES = "MINNESOTA TIMBERWOLVES"
    NEW_ORLEANS_PELICANS = "NEW ORLEANS PELICANS"
    NEW_YORK_KNICKS = "NEW YORK KNICKS"
    OKLAHOMA_CITY_THUNDER = "OKLAHOMA CITY THUNDER"
    ORLANDO_MAGIC = "ORLANDO MAGIC"
    PHILADELPHIA_76ERS = "PHILADELPHIA 76ERS"
    PHOENIX_SUNS = "PHOENIX SUNS"
    PORTLAND_TRAIL_BLAZERS = "PORTLAND TRAIL BLAZERS"
    SACRAMENTO_KINGS = "SACRAMENTO KINGS"
    SAN_ANTONIO_SPURS = "SAN ANTONIO SPURS"
    TORONTO_RAPTORS = "TORONTO RAPTORS"
    UTAH_JAZZ = "UTAH JAZZ"
    WASHINGTON_WIZARDS = "WASHINGTON WIZARDS"

    # DEPRECATED TEAMS
    CHARLOTTE_BOBCATS = "CHARLOTTE BOBCATS"
    NEW_JERSEY_NETS = "NEW JERSEY NETS"
    NEW_ORLEANS_HORNETS = "NEW ORLEANS HORNETS"
    NEW_ORLEANS_OKLAHOMA_CITY_HORNETS = "NEW ORLEANS/OKLAHOMA CITY HORNETS"
    SEATTLE_SUPERSONICS = "SEATTLE SUPERSONICS"
    VANCOUVER_GRIZZLIES = "VANCOUVER GRIZZLIES"


TEAM_NAME_TO_TEAM = {
    "ATLANTA_HAWKS": Team.ATLANTA_HAWKS,
    "BOSTON_CELTICS": Team.BOSTON_CELTICS,
    "BROOKLYN_NETS": Team.BROOKLYN_NETS,
    "CHARLOTTE_HORNETS": Team.CHARLOTTE_HORNETS,
    "CHICAGO_BULLS": Team.CHICAGO_BULLS,
    "CLEVELAND_CAVALIERS": Team.CLEVELAND_CAVALIERS,
    "DALLAS_MAVERICKS": Team.DALLAS_MAVERICKS,
    "DENVER_NUGGETS": Team.DENVER_NUGGETS,
    "DETROIT_PISTONS": Team.DETROIT_PISTONS,
    "GOLDEN_STATE_WARRIORS": Team.GOLDEN_STATE_WARRIORS,
    "HOUSTON_ROCKETS": Team.HOUSTON_ROCKETS,
    "INDIANA_PACERS": Team.INDIANA_PACERS,
    "LOS_ANGELES_CLIPPERS": Team.LOS_ANGELES_CLIPPERS,
    "LOS_ANGELES_LAKERS": Team.LOS_ANGELES_LAKERS,
    "MEMPHIS_GRIZZLIES": Team.MEMPHIS_GRIZZLIES,
    "MIAMI_HEAT": Team.MIAMI_HEAT,
    "MILWAUKEE_BUCKS": Team.MILWAUKEE_BUCKS,
    "MINNESOTA_TIMBERWOLVES": Team.MINNESOTA_TIMBERWOLVES,
    "NEW_ORLEANS_PELICANS": Team.NEW_ORLEANS_PELICANS,
    "NEW_YORK_KNICKS": Team.NEW_YORK_KNICKS,
    "OKLAHOMA_CITY_THUNDER": Team.OKLAHOMA_CITY_THUNDER,
    "ORLANDO_MAGIC": Team.ORLANDO_MAGIC,
    "PHILADELPHIA_76ERS": Team.PHILADELPHIA_76ERS,
    "PHOENIX_SUNS": Team.PHOENIX_SUNS,
    "PORTLAND_TRAIL_BLAZERS": Team.PORTLAND_TRAIL_BLAZERS,
    "SACRAMENTO_KINGS": Team.SACRAMENTO_KINGS,
    "SAN_ANTONIO_SPURS": Team.SAN_ANTONIO_SPURS,
    "TORONTO_RAPTORS": Team.TORONTO_RAPTORS,
    "UTAH_JAZZ": Team.UTAH_JAZZ,
    "WASHINGTON_WIZARDS": Team.WASHINGTON_WIZARDS,

    # DEPRECATED TEAMS
    "CHARLOTTE_BOBCATS": Team.CHARLOTTE_BOBCATS,
    "NEW_JERSEY_NETS": Team.NEW_JERSEY_NETS,
    "NEW_ORLEANS_HORNETS": Team.NEW_ORLEANS_HORNETS,
    "NEW_ORLEANS_OKLAHOMA_CITY_HORNETS": Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS,
    "SEATTLE_SUPERSONICS": Team.SEATTLE_SUPERSONICS,
    "VANCOUVER_GRIZZLIES": Team.VANCOUVER_GRIZZLIES,
}


TEAM_TO_TEAM_ABBREVIATIONS = {
    Team.ATLANTA_HAWKS:                     'ATL',
    Team.BOSTON_CELTICS:                    'BOS',
    Team.BROOKLYN_NETS:                     'BRK',
    Team.CHICAGO_BULLS:                     'CHI',
    Team.CHARLOTTE_HORNETS:                 'CHO',
    Team.CLEVELAND_CAVALIERS:               'CLE',
    Team.DALLAS_MAVERICKS:                  'DAL',
    Team.DENVER_NUGGETS:                    'DEN',
    Team.DETROIT_PISTONS:                   'DET',
    Team.GOLDEN_STATE_WARRIORS:             'GSW',
    Team.HOUSTON_ROCKETS:                   'HOU',
    Team.INDIANA_PACERS:                    'IND',
    Team.LOS_ANGELES_CLIPPERS:              'LAC',
    Team.LOS_ANGELES_LAKERS:                'LAL',
    Team.MEMPHIS_GRIZZLIES:                 'MEM',
    Team.MIAMI_HEAT:                        'MIA',
    Team.MILWAUKEE_BUCKS:                   'MIL',
    Team.MINNESOTA_TIMBERWOLVES:            'MIN',
    Team.NEW_ORLEANS_PELICANS:              'NOP',
    Team.NEW_YORK_KNICKS:                   'NYK',
    Team.OKLAHOMA_CITY_THUNDER:             'OKC',
    Team.ORLANDO_MAGIC:                     'ORL',
    Team.PHILADELPHIA_76ERS:                'PHI',
    Team.PHOENIX_SUNS:                      'PHO',
    Team.PORTLAND_TRAIL_BLAZERS:            'POR',
    Team.SACRAMENTO_KINGS:                  'SAC',
    Team.SAN_ANTONIO_SPURS:                 'SAS',
    Team.TORONTO_RAPTORS:                   'TOR',
    Team.UTAH_JAZZ:                         'UTA',
    Team.WASHINGTON_WIZARDS:                'WAS',

    # DEPRECATED TEAMS
    Team.NEW_JERSEY_NETS:                   'NJN',
    Team.NEW_ORLEANS_HORNETS:               'NOH',
    Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS: 'NOK',
    Team.CHARLOTTE_BOBCATS:                 'CHA',
    Team.SEATTLE_SUPERSONICS:               'SEA',
    Team.VANCOUVER_GRIZZLIES:               'VAN',
}


class Quarter(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    OVERTIME_1 = 5
    OVERTIME_2 = 6
    OVERTIME_3 = 7
    OVERTIME_4 = 8
    OVERTIME_5 = 9
    OVERTIME_6 = 10


class Make(Enum):
    MISS = 0
    MAKE = 1


class EventType(Enum):
    FREE_THROW = 1
    TWO_PTR = 2
    THREE_PTR = 3
    REBOUND = auto()
    FOUL = auto()
    TURNOVER = auto()
    VIOLATION = auto()
    TIMEOUT = auto()
    ENTERS_THE_GAME = auto()
    JUMP_BALL = auto()
    QUARTER_START_END = auto()
    INSTANT_REPLAY = auto()
    EJECTION = auto()
    OTHER = 999


class Position:
    def __init__(self, top, left):
        self.top = top
        self.left = left

    def __str__(self):
        return "Top: " + self.top + ", Left: " + self.left


class GameTime:
    def __init__(self, quarter, time_left):
        if quarter is None or time_left is None:
            print("None input in GameTime")

        self.quarter = quarter
        self.time_left = time_left

    def __str__(self):
        return "Quarter: " + str(self.quarter) + ", Time Remaining: " + self.time_left


class Score:
    def __init__(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score


class Event:
    def __init__(self, time, relevant_team, score, description, event_type):
        self.time = time
        self.relevant_team = relevant_team
        self.score = score
        self.description = description
        self.event_type = event_type


class FreeThrow(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 player, make, shot_number, total_num_shots):
        super().__init__(time, relevant_team, score, description, event_type)
        self.player = player
        self.make = make
        self.shot_number = shot_number
        self.total_num_shots = total_num_shots


class FieldGoal(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 player, make, blocked_by, assist_by, distance, position):
        super().__init__(time, relevant_team, score, description, event_type)
        self.player = player
        self.make = make
        self.blocked_by = blocked_by
        self.assist_by = assist_by
        self.distance = distance
        self.position = position

    def __str__(self):
        if self.make == Make.MAKE:
            made_str = "made"
        else:
            made_str = "missed"
        return "Shot of type " + str(self.event_type) + \
               " " + made_str + \
               " at " + str(self.time) + \
               " by " + self.player + \
               " at position " + str(self.position)


class ReboundType(Enum):
    DEFENSIVE = 0,
    OFFENSIVE = 1


class Rebound(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 player, rebound_type):
        super().__init__(time, relevant_team, score, description, event_type)
        self.player = player
        self.rebound_type = rebound_type


class FoulType(Enum):
    SHOOTING = auto()
    LOOSE_BALL = auto()
    PERSONAL = auto()
    DEF_THREE_SECOND = auto()
    FLAGRANT = auto()
    OFFENSIVE = auto()
    BLOCKING = auto()
    CHARGING = auto()
    DEFENSIVE = auto()
    DOUBLE = auto()
    ILLEGAL_SCREEN = auto()
    INTENTIONAL = auto()
    PUNCHING = auto()
    REACH_IN = auto()
    TECHNICAL = auto()
    TAKE = auto()
    AWAY_FROM_PLAY = auto()
    CLEAR_PATH = auto()
    OTHER = 999


class Foul(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 player, drawn_by, foul_type):
        super().__init__(time, relevant_team, score, description, event_type)
        self.player = player
        self.drawn_by = drawn_by
        self.foul_type = foul_type


class TurnoverType(Enum):
    BAD_PASS = auto()
    LOST_BALL = auto()
    OFFENSIVE_FOUL = auto()
    TRAVELING = auto()
    SHOT_CLOCK = auto()
    OUT_OF_BOUNDS_LOST_BALL = auto()
    STEP_OUT_OF_BOUNDS = auto()
    THREE_SECOND = auto()
    FIVE_SECOND = auto()
    EIGHT_SECOND = auto()
    BACK_COURT = auto()
    DISCONTINUED_DRIBBLE = auto()
    INBOUND = auto()
    OFFENSIVE_GOALTENDING = auto()
    OTHER = 999


class Turnover(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 player, steal_by, turnover_type):
        super().__init__(time, relevant_team, score, description, event_type)
        self.player = player
        self.steal_by = steal_by
        self.turnover_type = turnover_type


class ViolationType(Enum):
    KICKED_BALL = auto()
    DELAY_OF_GAME = auto()
    DEFENSIVE_GOALTENDING = auto()
    OTHER = 999


class Violation(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 player, violation_type):
        super().__init__(time, relevant_team, score, description, event_type)
        self.player = player
        self.violation_type = violation_type


class TimeoutType(Enum):
    FULL = auto()
    OFFICIAL = auto()
    TWENTY_SECOND = auto()
    OTHER = 999


class Timeout(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 timeout_type):
        super().__init__(time, relevant_team, score, description, event_type)
        self.timeout_type = timeout_type


class EntersTheGame(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 entering_player, subbed_player):
        super().__init__(time, relevant_team, score, description, event_type)
        self.entering_player = entering_player
        self.subbed_player = subbed_player


class QuarterStartOrEnd(Event):
    def __init__(self, time, relevant_team, score, description, event_type):
        super().__init__(time, relevant_team, score, description, event_type)


class JumpBall(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 home_player, away_player, gains_possession):
        super().__init__(time, relevant_team, score, description, event_type)
        self.home_player = home_player
        self.away_player = away_player
        self.gains_possession = gains_possession


class InstantReplayType(Enum):
    CHALLENGE = auto()
    REQUEST = auto()
    OTHER = 999


class InstantReplayOutcome(Enum):
    STANDS = 1
    OVERTURNED = 0


class InstantReplay(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 replay_type, outcome):
        super().__init__(time, relevant_team, score, description, event_type)
        self.replay_type = replay_type
        self.outcome = outcome


class Ejection(Event):
    def __init__(self, time, relevant_team, score, description, event_type,
                 player):
        super().__init__(time, relevant_team, score, description, event_type)
        self.player = player


class Player:
    def __init__(self, ref_tag, full_name):
        self.ref_tag = ref_tag
        self.full_name = full_name
