from enum import Enum, auto, IntEnum

from gametime import GameTime
from teams import Team


class Quarter(IntEnum):
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


QTR_STR_TO_QTR = {
    "Quarter.FIRST": Quarter.FIRST,
    "Quarter.SECOND": Quarter.SECOND,
    "Quarter.THIRD": Quarter.THIRD,
    "Quarter.FOURTH": Quarter.FOURTH,
    "Quarter.OVERTIME_1": Quarter.OVERTIME_1,
    "Quarter.OVERTIME_2": Quarter.OVERTIME_2,
    "Quarter.OVERTIME_3": Quarter.OVERTIME_3,
    "Quarter.OVERTIME_4": Quarter.OVERTIME_4,
    "Quarter.OVERTIME_5": Quarter.OVERTIME_5,
    "Quarter.OVERTIME_6": Quarter.OVERTIME_6
}


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


class Score:
    def __init__(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score


class Event:
    def __init__(self, time: GameTime, relevant_team: Team, score: Score, description: str, event_type: EventType):
        self.time = time
        self.relevant_team = relevant_team
        self.score = score
        self.description = description
        self.event_type = event_type

    def __str__(self):
        return "Event type: " + str(self.event_type) + " at " + str(self.time)

    @staticmethod
    def compile_events(events):
        compiled_events = []
        i = 0
        while i < len(events):
            event = events[i]
            event_list = [event]
            i += 1
            for j in range(i, len(events)):
                next_event = events[j]
                if event.time == next_event.time:
                    event_list.append(next_event)
                    i = j + 1
            compiled_events.append(event_list)
        return compiled_events


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
               " by " + self.player.full_name + \
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
