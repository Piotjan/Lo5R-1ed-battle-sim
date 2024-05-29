"""
Module with common functions for project.
"""
import random

from structures_enums import dices_in_roll


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
    rolls.sort()
    biggest_rolls = rolls[-dices_to_sum:]
    rolls_sum = sum(biggest_rolls)
    return rolls_sum
