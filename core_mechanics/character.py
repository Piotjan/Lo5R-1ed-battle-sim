"""
Module with character class.
"""
from utilities import BattleLine
from utilities import RingsNames


class Character:
    """Representation of character in mechanichs

    this virtual class is an representation of nay kind of character,
    playable or not.

    Fields:

    """

    def __init__(self, name: str, line: BattleLine, rings: dict, hp_levels: int) -> None:
        self.name = name
        self.line = line
        self.rings = rings
        self.hp_levels = hp_levels
        self.hp_per_lvl = self._calculate_hp_pr_lvl()

    def _calculate_hp_pr_lvl(self) -> int:
        """Method calculates Hit Poitns per level.

        This method calculates Hit Points per level based on Earth Ring.
        It is multipled by 2, according to rule book.

        Returns:
            int: Amount of hit points per level.
        """
        return self.rings[RingsNames.EARTH].get_ring_value() * 2
