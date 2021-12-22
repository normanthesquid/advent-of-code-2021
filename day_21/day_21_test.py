import unittest
from part1 import play
from part2 import play_dirac, branch_game
from deterministic_die import DeterministicDie


class TestDay21(unittest.TestCase):
    def test_game_with_test_starts(self):
        """
        Play the game using the test inputs
        """
        player_one_start = 4
        player_two_start = 8
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start
        )
        self.assertEqual(player_one_score, 1000)
        self.assertEqual(player_two_score, 745)
        self.assertEqual(roll_count, 993)
        self.assertEqual(roll_count * player_two_score, 739785)

    def test_first_turn_with_test_starts(self):
        """
        Verify the game state after the first turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 1
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 10)
        self.assertEqual(player_two_score, 0)
        self.assertEqual(roll_count, 3)

    def test_second_turn_with_test_starts(self):
        """
        Verify the game state after the second turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 2
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 10)
        self.assertEqual(player_two_score, 3)
        self.assertEqual(roll_count, 6)

    def test_third_turn_with_test_starts(self):
        """
        Verify the game state after the third turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 3
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 14)
        self.assertEqual(player_two_score, 3)
        self.assertEqual(roll_count, 9)

    def test_fourth_turn_with_test_starts(self):
        """
        Verify the game state after the fourth turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 4
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 14)
        self.assertEqual(player_two_score, 9)
        self.assertEqual(roll_count, 12)

    def test_fifth_turn_with_test_starts(self):
        """
        Verify the game state after the fifth turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 5
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 20)
        self.assertEqual(player_two_score, 9)
        self.assertEqual(roll_count, 15)

    def test_sixth_turn_with_test_starts(self):
        """
        Verify the game state after the sixth turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 6
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 20)
        self.assertEqual(player_two_score, 16)
        self.assertEqual(roll_count, 18)

    def test_seventh_turn_with_test_starts(self):
        """
        Verify the game state after the seventh turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 7
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 26)
        self.assertEqual(player_two_score, 16)
        self.assertEqual(roll_count, 21)

    def test_eighth_turn_with_test_starts(self):
        """
        Verify the game state after the eighth turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 8
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 26)
        self.assertEqual(player_two_score, 22)
        self.assertEqual(roll_count, 24)

    def test_330nd_turn_with_test_starts(self):
        """
        Verify the game state after the 992nd turn
        """
        player_one_start = 4
        player_two_start = 8
        turn_limit = 330
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start, turn_limit
        )
        self.assertEqual(player_one_score, 990)
        self.assertEqual(player_two_score, 745)
        self.assertEqual(roll_count, 990)

    def test_game_with_actual_starts(self):
        """
        Play the game using the real inputs
        """
        player_one_start = 1
        player_two_start = 10
        [roll_count, player_one_score, player_two_score] = play(
            player_one_start, player_two_start
        )
        self.assertNotEqual(roll_count, None)
        self.assertNotEqual(player_one_score, None)
        self.assertNotEqual(player_two_score, None)
        losing_score = min(player_one_score, player_two_score)
        result = roll_count * losing_score
        print("\ngame result:", result)

    def test_deterministic_die_first_roll(self):
        """
        Make sure the die rolls 1 on the first roll
        """

        die = DeterministicDie()
        result = die.roll()
        self.assertEqual(result, 1)

    def test_deterministic_die_second_roll(self):
        """
        Make sure the die rolls 2 on the second roll
        """

        die = DeterministicDie()
        result = die.roll()
        result = die.roll()
        self.assertEqual(result, 2)

    def test_deterministic_die_100th_roll(self):
        """
        Make sure the die rolls 100 on the 100th roll
        """

        die = DeterministicDie()
        for i in range(100):
            result = die.roll()

        self.assertEqual(result, 100)

    def test_deterministic_die_101st_roll(self):
        """
        Make sure the die rolls 1 on the 101st roll
        """

        die = DeterministicDie()
        for i in range(101):
            result = die.roll()

        self.assertEqual(result, 1)

    def test_deterministic_die_202nd_roll(self):
        """
        Make sure the die rolls 2 on the 202nd roll
        """

        die = DeterministicDie()
        for i in range(202):
            result = die.roll()

        self.assertEqual(result, 2)

    def test_dirac_game_with_test_starts(self):
        """
        Play the game using the test inputs
        """
        player_one_start = 4
        player_two_start = 8
        [player_one_wins, player_two_wins] = play_dirac(
            player_one_start, player_two_start
        )
        self.assertEqual(player_one_wins, 444356092776315)
        self.assertEqual(player_two_wins, 341960390180808)

    def test_dirac_game_with_actual_starts(self):
        """
        Play the game using the test inputs
        """
        player_one_start = 1
        player_two_start = 10
        [player_one_wins, player_two_wins] = play_dirac(
            player_one_start, player_two_start
        )

        print("\nplayer_one_wins:", player_one_wins)
        print("player_two_wins:", player_two_wins)


if __name__ == "__main__":
    unittest.main()
