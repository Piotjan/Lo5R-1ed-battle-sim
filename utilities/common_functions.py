"""
Module with common functions for project.
"""
import random
from pathlib import Path

from .structures_enums_classes import dices_in_roll


def roll_dices(dices: dices_in_roll) -> int:
    """
    Function simulates standard dice rolls of whole dice set.
    """
    roll_results = []
    for dice in range(dices.start_amount):
        new_roll_result = make_single_roll()
        roll_results.append(new_roll_result)
    roll_sum = make_sum_from_rolls(rolls=roll_results, dices_to_sum=dices.remain)
    return roll_sum


def make_single_roll() -> int:
    """
    Functions gets result of rolling d10.
    Tens are rerolled and added to the result.
    """
    final_sum = 0
    while True:
        current_roll = random.randint(1, 10)
        final_sum += current_roll
        if not current_roll == 10:
            break
    return final_sum


def make_sum_from_rolls(rolls: list[int], dices_to_sum: int) -> int:
    """
    Functions sums the biggest rolls results.
    """
    if dices_to_sum == 0:
        raise AttributeError('Dices to remain has to be bigger than 0!')
    if len(rolls) < dices_to_sum:
        raise AttributeError(f'Cannot sum more dices ({dices_to_sum}) than made rolls ({len(rolls)})')
    rolls.sort()
    biggest_rolls = rolls[-dices_to_sum:]
    rolls_sum = sum(biggest_rolls)
    return rolls_sum


def create_directory(path_to_create: Path) -> None:
    """Function creates new directory.

    This unction creates new directory. It should not be a file path.

    Args:
        path_to_create (Path): Path to create.

    Raises:
        ValueError: In case of passing path to file.] instead of directory.
    """
    if path_to_create.suffix:
        raise ValueError(f'Cannot create directory form filepath: {path_to_create.as_posix()}!')
    else:
        path_to_create.mkdir(parents=True, exist_ok=True)
