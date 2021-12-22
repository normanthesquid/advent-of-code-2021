import time
from day_21.deterministic_die import DeterministicDie


def play(
    player_one_position: int, player_two_position: int, turn_limit: int = None
) -> int:

    player_one_score = 0
    player_two_score = 0
    roll_count = 0
    turn_count = 0
    player_one_turn = True

    die = DeterministicDie()

    # zero index positions
    player_one_position = player_one_position - 1
    player_two_position = player_two_position - 1

    while player_one_score < 1000 and player_two_score < 1000:
        turn_count += 1
        roll_count += 3
        if player_one_turn:
            player_one_position = (
                player_one_position + die.roll() + die.roll() + die.roll()
            )
            player_one_position = player_one_position % 10

            player_one_score += player_one_position + 1
        else:
            player_two_position = (
                player_two_position + die.roll() + die.roll() + die.roll()
            )
            player_two_position = player_two_position % 10

            player_two_score += player_two_position + 1
        player_one_turn = not player_one_turn

        if turn_limit is not None and turn_limit == turn_count:
            break

    return [roll_count, player_one_score, player_two_score]


if __name__ == "__main__":
    start_time = time.time()
    play()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
