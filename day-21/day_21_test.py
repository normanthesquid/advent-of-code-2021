import unittest
from part1 import play
from deterministic_dice import DeterministicDice


class TestDay21(unittest.TestCase):
    def test_game_with_test_starts(self):
        """
        Play the game using the test inputs
        """
        player_one_start = 4
        player_two_start = 8
        result = play(player_one_start, player_two_start)
        self.assertEqual(result, 739785)

    def test_game_with_actual_starts(self):
        """
        Play the game using the real inputs
        """
        player_one_start = 1
        player_two_start = 10
        result = play(player_one_start, player_two_start)
        self.assertNotEqual(result, None)
        print("game result:", result)

    def test_deterministic_dice_first_roll(self):
        """
        Make sure the die rolls 1 on the first roll
        """

        dice = DeterministicDice()
        result = dice.roll()
        self.assertEqual(result, 1)

    def test_deterministic_dice_second_roll(self):
        """
        Make sure the die rolls 2 on the second roll
        """

        dice = DeterministicDice()
        result = dice.roll()
        result = dice.roll()
        self.assertEqual(result, 2)

    def test_deterministic_dice_100th_roll(self):
        """
        Make sure the die rolls 100 on the 100th roll
        """

        dice = DeterministicDice()
        for i in range(100):
            result = dice.roll()

        self.assertEqual(result, 100)

    def test_deterministic_dice_101st_roll(self):
        """
        Make sure the die rolls 1 on the 101st roll
        """

        dice = DeterministicDice()
        for i in range(101):
            result = dice.roll()

        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
