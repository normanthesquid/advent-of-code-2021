import unittest
from part1 import play


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
        Play the game using the test inputs
        """
        player_one_start = 1
        player_two_start = 10
        result = play(player_one_start, player_two_start)
        self.assertNotEqual(result, None)


if __name__ == "__main__":
    unittest.main()
