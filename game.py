"""
Game class - dataclass for lottery game info
"""
from dataclasses import dataclass, field
from enum import Enum, auto

from dateutil import parser as date

from drawing import Drawing


class Day(Enum):
    """ Days of the week. """
    SUNDAY = auto()
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()


@dataclass
class Game:
    """
    Class for lottery game information
    """
    name: str
    field_num_max: int
    bonus_ball_max: int
    time_drawn: str
    analysis_start_date: str
    days_drawn: list[Day] = field(default_factory=list)
    history: list[Drawing] = field(default_factory=list)

    def __post_init__:



    def set_analysis_start_date:
        analysis_start_date = date.parse(timestr=ana fuzzy=True)
