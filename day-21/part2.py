import time
from typing import List
from functools import cache
from itertools import product


def play_dirac(
    player_one_position: int,
    player_two_position: int,
) -> List:

    # zero index positions
    player_one_position = player_one_position - 1
    player_two_position = player_two_position - 1

    return branch_game(False, player_one_position, 0, player_two_position, 0)


@cache
def branch_game(
    player_one_turn,
    player_one_position,
    player_one_score,
    player_two_position,
    player_two_score,
) -> List:
    if player_one_score >= 21:
        return [1, 0]
    if player_two_score >= 21:
        return [0, 1]
    branch_results = []
    player_one_turn = not player_one_turn
    if player_one_turn:
        for position in roll_dice(player_one_position):
            branch_results.append(
                branch_game(
                    player_one_turn,
                    position,
                    player_one_score + position + 1,
                    player_two_position,
                    player_two_score,
                )
            )
    else:
        for position in roll_dice(player_two_position):
            branch_results.append(
                branch_game(
                    player_one_turn,
                    player_one_position,
                    player_one_score,
                    position,
                    player_two_score + position + 1,
                )
            )

    result = [0, 0]
    for branch_result in branch_results:
        result[0] += branch_result[0]
        result[1] += branch_result[1]
    return result


sides = [1, 2, 3]
rolls = [sum(x) for x in product(sides, repeat=3)]


@cache
def roll_dice(position: int):
    results = []
    for roll in rolls:
        results.append((position + roll) % 10)
    return results


if __name__ == "__main__":
    start_time = time.time()
    play_dirac()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
