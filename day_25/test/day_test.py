import unittest

from day_25.part1 import move_herds, read_input


class TestDay25(unittest.TestCase):
    def test_input_parsed_correctly(self):
        """
        Make sure input instruction can be parsed correctly
        """
        grid = read_input(True)

        cucumbers = list(
            filter(lambda cell: cell.south_cucumber or cell.east_cucumber, grid)
        )

        self.assertEquals(len(grid), 90)
        self.assertEquals(len(cucumbers), 49)

    def test_neighbors_built_correctly(self):
        """
        Make sure neighbor links are built correctly
        """

        grid = read_input(True)

        built_correctly = True

        for cell in grid:
            if len(cell.neighbors) != 4:
                built_correctly = False
                break

        self.assertTrue(built_correctly)

    def test_example_herd_moves_correctly(self):
        """
        Make sure example herds stop when they are supposed to
        """

        last_step = move_herds(True)

        self.assertEquals(last_step, 58)

    def test_herd_moves_correctly(self):
        """
        Make sure herds stop when they are supposed to
        """

        last_step = move_herds(False)

        self.assertEquals(last_step, 568)


if __name__ == "__main__":
    unittest.main()
