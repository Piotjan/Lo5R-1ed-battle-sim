"""
Module with common enumes and structures.
"""
from collections import namedtuple
from enum import Enum

dices_in_roll = namedtuple('dices_in_roll', ['start_amount', 'remain'])


# Enums
class CharacterAttributes(Enum):
    """
    Enum which relfexes in game chareacters statistics.
    """
    CONSTITUTION = 1
    WILL_POWER = 2
    AGILITY = 3
    INTELIGENCE = 4
    REFLEX = 5
    INTUITION = 6
    STRENGTH = 7
    PERCEPTIVITY = 8
    VOID_POINTS = 9


class RingsNames(Enum):
    """
    Enum with 5 basic elemnts names
    """
    EARTH = 1
    FIRE = 2
    WATER = 3
    AIR = 4
    VOID = 5
