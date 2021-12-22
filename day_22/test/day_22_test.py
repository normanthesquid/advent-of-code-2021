import unittest
from day_22.instruction import Instruction


class TestDay21(unittest.TestCase):
    def test_instruction_construction_range(self):
        """
        Make sure instructions build their range correctly
        """
        instruction = Instruction("on x=10..12,y=10..12,z=10..12")

        self.assertEqual(instruction.x_start, 10)
        self.assertEqual(instruction.x_end, 12)
        self.assertEqual(instruction.y_start, 10)
        self.assertEqual(instruction.y_end, 12)
        self.assertEqual(instruction.z_start, 10)
        self.assertEqual(instruction.z_end, 12)

    


if __name__ == "__main__":
    unittest.main()
