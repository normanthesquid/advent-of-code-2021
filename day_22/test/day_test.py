import unittest
from day_22.instruction import Instruction


class TestDay21(unittest.TestCase):
    def test_instruction_construction_on(self):
        """
        Make sure instructions set on correctly
        """
        instruction = Instruction("on x=10..12,y=10..12,z=10..12")

        self.assertTrue(instruction.on)  

    def test_instruction_construction_off(self):
        """
        Make sure instructions set off correctly
        """
        instruction = Instruction("off x=10..12,y=10..12,z=10..12")

        self.assertFalse(instruction.on)      

    def test_instruction_construction_range(self):
        """
        Make sure instructions build their range correctly
        """
        instruction = Instruction("on x=10..12,y=11..13,z=12..14")

        self.assertEqual(instruction.x_start, 10)
        self.assertEqual(instruction.x_end, 12)
        self.assertEqual(instruction.y_start, 11)
        self.assertEqual(instruction.y_end, 13)
        self.assertEqual(instruction.z_start, 12)
        self.assertEqual(instruction.z_end, 14)

    def test_instruction_construction_affected_cubes(self):
        """
        Make sure instructions build their affected_cubes
        """
        instruction = Instruction("on x=10..12,y=10..12,z=10..12")

        self.assertEqual(len(instruction.affected_cubes), 27)   

    def test_instruction_construction_x_below_of_space_range(self):
        """
        Make sure instructions don't affect any cubes below a limited space in the x direction
        """
        instruction = Instruction("on x=-54112..-39298,y=-10..-10,z=-10..10", 50)

        self.assertEqual(len(instruction.affected_cubes), 0)

    def test_instruction_construction_x_above_of_space_range(self):
        """
        Make sure instructions don't affect any cubes above a limited space in the x direction
        """
        instruction = Instruction("on x=34112..39298,y=-10..-10,z=-10..10", 50)

        self.assertEqual(len(instruction.affected_cubes), 0) 

    def test_instruction_construction_x_partial_space_range(self):
        """
        Make sure instructions don't affect any cubes outside a limited space in the x direction
        """
        instruction = Instruction("on x=-51..-49,y=0..0,z=0..0", 50)

        self.assertEqual(len(instruction.affected_cubes), 2) 

    def test_instruction_construction_y_out_of_space_range(self):
        """
        Make sure instructions don't affect any cubes outside a limited space in the y direction
        """
        instruction = Instruction("on x=-10..-10,y=-70..-60,z=-10..10", 50)

        self.assertEqual(len(instruction.affected_cubes), 0) 

    def test_instruction_construction_y_partial_space_range(self):
        """
        Make sure instructions don't affect any cubes outside a partial limited space in the y direction
        """
        instruction = Instruction("on x=-10..-10,y=-51..-49,z=0..0", 50)

        self.assertEqual(len(instruction.affected_cubes), 2) 

    def test_instruction_construction_z_out_of_space_range(self):
        """
        Make sure instructions don't affect any cubes outside a limited space in the z direction
        """
        instruction = Instruction("on x=-10..10,y=-10..10,z=-27449..-7877", 50)

        self.assertEqual(len(instruction.affected_cubes), 0) 

    def test_instruction_construction_z_partial_space_range(self):
        """
        Make sure instructions don't affect any cubes outside a partial limited space in the z direction
        """
        instruction = Instruction("on x=0..0,y=0..0,z=-51..-49", 50)

        self.assertEqual(len(instruction.affected_cubes), 2) 


if __name__ == "__main__":
    unittest.main()
