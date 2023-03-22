import unittest

from shulker.components.Coordinates import Coordinates, WrongCaretNotation

class TestCoordinates(unittest.TestCase):
    def test_init(self):
        """
        This test checks if the Coordinates class initializes correctly 
        with only x, y, and z values provided. It ensures that the x, y, and z 
        values are assigned correctly, and yaw and pitch are set to None by default.
        """
        
        coords = Coordinates(1, 2, 3)
        self.assertEqual(coords.x, 1)
        self.assertEqual(coords.y, 2)
        self.assertEqual(coords.z, 3)
        self.assertIsNone(coords.yaw)
        self.assertIsNone(coords.pitch)

    def test_init_with_yaw_and_pitch(self):
        """
        This test checks if the Coordinates class initializes correctly when 
        x, y, z, yaw, and pitch values are provided. It ensures that all the 
        values are assigned correctly.
        """
        
        coords = Coordinates(1, 2, 3, 90, 45)
        self.assertEqual(coords.x, 1)
        self.assertEqual(coords.y, 2)
        self.assertEqual(coords.z, 3)
        self.assertEqual(coords.yaw, 90)
        self.assertEqual(coords.pitch, 45)

    def test_check_carets_valid(self):
        """
        This test verifies that the check_carets() method works correctly 
        when all coordinates use caret notation. 
        It should not raise a WrongCaretNotation exception in this case.
        """
        
        coords = Coordinates("^1", "^2", "^3")
        try:
            coords.check_carets()
        except WrongCaretNotation:
            self.fail("check_carets() raised WrongCaretNotation unexpectedly")

    def test_check_carets_invalid(self):
        """
        This test verifies that the check_carets() method raises a WrongCaretNotation
        exception when only some of the coordinates use caret notation,
        which is an invalid case.
        """
        
        coords = Coordinates(1, "^2", 3)
        with self.assertRaises(WrongCaretNotation):
            coords.check_carets()

    def test_offset_without_yaw_and_pitch(self):
        """
        This test checks if the offset() method correctly offsets the x, y, and z values
        when yaw and pitch are not provided. It ensures that the resulting object
        has the correct updated values for x, y, and z.
        """
        
        coords = Coordinates(1, 2, 3)
        new_coords = coords.offset(1, 1, 1)
        self.assertEqual(new_coords.x, 2)
        self.assertEqual(new_coords.y, 3)
        self.assertEqual(new_coords.z, 4)
        self.assertIsNone(new_coords.yaw)
        self.assertIsNone(new_coords.pitch)

    def test_offset_with_yaw_and_pitch(self):
        """
        This test checks if the offset() method correctly offsets the x, y, z, yaw, and pitch values
        when yaw and pitch are provided. It ensures that the resulting object has the correct
        updated values for all parameters.
        """
        
        coords = Coordinates(1, 2, 3, 90, 45)
        new_coords = coords.offset(1, 1, 1, 10, 5)
        self.assertEqual(new_coords.x, 2)
        self.assertEqual(new_coords.y, 3)
        self.assertEqual(new_coords.z, 4)
        self.assertEqual(new_coords.yaw, 100)
        self.assertEqual(new_coords.pitch, 50)

    def test_str_without_yaw_and_pitch(self):
        """
        This test verifies that the __str__() method returns the correct string
        representation of the Coordinates object when yaw and pitch are not provided.
        It checks if the output string has the correct format and values for x, y, and z.
        """
        
        coords = Coordinates(1, 2, 3)
        self.assertEqual(str(coords), "1 2 3")

    def test_str_with_yaw_and_pitch(self):
        """
        This test verifies that the __str__() method returns the correct string representation
        of the Coordinates object when yaw and pitch are provided. 
        It checks if the output string has the correct format and 
        values for x, y, z, yaw, and pitch.
        """
        
        coords = Coordinates(1, 2, 3, 90, 45)
        self.assertEqual(str(coords), "1 2 3 90 45")

    def test_str_with_caret_notation(self):
        """
        This test verifies that the __str__() method returns the correct string representation
        of the Coordinates object when using caret notation for x, y, and z.
        It checks if the output string has the correct format and values.
        """
        
        coords = Coordinates("^1", "^2", "^3")
        self.assertEqual(str(coords), "^1 ^2 ^3")

    def test_str_with_caret_notation_and_yaw_and_pitch(self):
        """
        This test verifies that the __str__() method returns the correct string representation
        of the Coordinates object when using caret notation for x, y, z,
        and providing yaw and pitch values. It checks if the output string
        has the correct format and values.
        """
        
        coords = Coordinates("^1", "^2", "^3", 90, 45)
        self.assertEqual(str(coords), "^1 ^2 ^3 90 45")

    def test_init_with_floats(self):
        """
        This test checks if the Coordinates class initializes correctly when x, y, and z values
        are provided as floats. It ensures that the x, y, and z values are assigned correctly.
        """
        
        coords = Coordinates(1.5, 2.5, 3.5)
        self.assertEqual(coords.x, 1.5)
        self.assertEqual(coords.y, 2.5)
        self.assertEqual(coords.z, 3.5)

    def test_init_with_strings(self):
        """
        This test checks if the Coordinates class initializes correctly when x, y, and z values
        are provided as strings. It ensures that the x, y, and z values are assigned correctly.
        """
        
        coords = Coordinates("1", "2", "3")
        self.assertEqual(coords.x, "1")
        self.assertEqual(coords.y, "2")
        self.assertEqual(coords.z, "3")

    def test_init_with_mixed_types(self):
        """
        This test checks if the Coordinates class initializes correctly when x, y, and z values
        are provided as a mix of integers, floats, and strings.
        It ensures that the x, y, and z values are assigned correctly.
        """
        
        coords = Coordinates("1", 2.5, 3)
        self.assertEqual(coords.x, "1")
        self.assertEqual(coords.y, 2.5)
        self.assertEqual(coords.z, 3)

    def test_offset_with_floats(self):
        """
        This test checks if the offset() method correctly offsets the x, y, and z values
        when the coordinates and offset values are floats.
        It ensures that the resulting object has the correct updated values for x, y, and z.
        """
        
        coords = Coordinates(1.5, 2.5, 3.5)
        new_coords = coords.offset(0.5, 0.5, 0.5)
        self.assertEqual(new_coords.x, 2)
        self.assertEqual(new_coords.y, 3)
        self.assertEqual(new_coords.z, 4)

    def test_str_with_floats(self):
        """
        This test verifies that the __str__() method returns the correct string representation
        of the Coordinates object when x, y, and z are floats.
        It checks if the output string has the correct format and values for x, y, and z.
        """
        
        coords = Coordinates(1.5, 2.5, 3.5)
        self.assertEqual(str(coords), "1.5 2.5 3.5")

    def test_str_with_strings(self):
        """
        This test verifies that the __str__() method returns the correct string representation
        of the Coordinates object when x, y, and z are strings.
        It checks if the output string has the correct format and values for x, y, and z.
        """
        
        coords = Coordinates("1", "2", "3")
        self.assertEqual(str(coords), "1 2 3")

    def test_str_with_mixed_types(self):
        """
        This test verifies that the __str__() method returns the correct string
        representation of the Coordinates object when x, y, and z values
        are a mix of integers, floats, and strings.
        It checks if the output string has the correct format and values.
        """
        
        coords = Coordinates("1", 2.5, 3)
        self.assertEqual(str(coords), "1 2.5 3")
    
    def test_init_with_negative_values(self):
        """
        This test checks if the Coordinates class initializes correctly when
        x, y, z, yaw, and pitch values are provided as negative numbers.
        It ensures that all the values are assigned correctly.
        """
        
        coords = Coordinates(-1, -2, -3, -90, -45)
        self.assertEqual(coords.x, -1)
        self.assertEqual(coords.y, -2)
        self.assertEqual(coords.z, -3)
        self.assertEqual(coords.yaw, -90)
        self.assertEqual(coords.pitch, -45)

    def test_offset_with_negative_values(self):
        """
        This test checks if the offset() method correctly offsets the
        x, y, and z values when the offset values are negative.
        It ensures that the resulting object has the correct updated
        values for x, y, and z.
        """
        
        coords = Coordinates(1, 2, 3)
        new_coords = coords.offset(-1, -1, -1)
        self.assertEqual(new_coords.x, 0)
        self.assertEqual(new_coords.y, 1)
        self.assertEqual(new_coords.z, 2)

    def test_init_with_float_yaw_and_pitch(self):
        """
        This test checks if the Coordinates class initializes correctly
        when yaw and pitch values are provided as floats.
        It ensures that the yaw and pitch values are assigned correctly.
        """
        
        coords = Coordinates(1, 2, 3, 90.5, 45.5)
        self.assertEqual(coords.x, 1)
        self.assertEqual(coords.y, 2)
        self.assertEqual(coords.z, 3)
        self.assertEqual(coords.yaw, 90.5)
        self.assertEqual(coords.pitch, 45.5)

    def test_init_with_string_yaw_and_pitch(self):
        """
        This test checks if the Coordinates class initializes correctly
        when yaw and pitch values are provided as strings.
        It ensures that the yaw and pitch values are assigned correctly.
        """
        
        coords = Coordinates(1, 2, 3, "90", "45")
        self.assertEqual(coords.x, 1)
        self.assertEqual(coords.y, 2)
        self.assertEqual(coords.z, 3)
        self.assertEqual(coords.yaw, "90")
        self.assertEqual(coords.pitch, "45")

