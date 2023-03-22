import unittest

from nbtlib import serialize_tag, Compound

from shulker.components.NBT import NBT
from shulker.components.Block import Block

class TestBlock(unittest.TestCase):
    def test_init_empty(self):
        """This test checks that an empty NBT object is properly initialized."""
        nbt = NBT()
        self.assertEqual(str(nbt), "{}")

    def test_init_compound(self):
        """This test checks that NBT object is initialized with Compound input."""
        compound = Compound({"test_key": "test_value"})
        nbt = NBT(compound)
        self.assertEqual(str(nbt), '{test_key:"test_value"}')

    def test_init_str(self):
        """This test checks that NBT object is initialized with string input."""
        nbt_str = '{"test_key": "test_value"}'
        nbt = NBT(nbt_str)
        self.assertEqual(str(nbt), '{test_key:"test_value"}')

    def test_init_dict(self):
        """This test checks that NBT object is initialized with dictionary input."""
        nbt_dict = {"test_key": "test_value"}
        nbt = NBT(nbt_dict)
        self.assertEqual(str(nbt), '{test_key:"test_value"}')

    def test_init_invalid_type(self):
        """This test checks that ValueError is raised with invalid input type."""
        with self.assertRaises(ValueError):
            NBT(["invalid", "input"])

    def test_setattr(self):
        """This test checks that attributes are properly set and converted to NBT."""
        nbt = NBT()
        nbt.test_key = "test_value"
        self.assertEqual(str(nbt), '{test_key:"test_value"}')

    def test_str(self):
        """This test checks that NBT object is serialized correctly to string."""
        nbt = NBT()
        nbt.test_key = "test_value"
        nbt_repr = str(nbt)
        self.assertEqual(nbt_repr, '{test_key:"test_value"}')
        
    def test_set_attribute_different_types(self):
        """
        This test checks that setting attributes of different types on an NBT
        object works correctly and updates the string representation.
        """
        
        nbt = NBT()
        nbt.int_value = 42
        nbt.float_value = 3.14
        nbt.str_value = "hello"
        self.assertEqual(serialize_tag(nbt.int_value, compact=True), "42")
        self.assertEqual(serialize_tag(nbt.float_value, compact=True), "3.14d")
        self.assertEqual(serialize_tag(nbt.str_value, compact=True), '"hello"')

    def test_update_attribute(self):
        """
        This test checks that updating an existing attribute
        on an NBT object results in the expected string representation.
        """
        
        nbt = NBT({"key": "value"})
        nbt.key = "new_value"
        self.assertEqual(str(nbt), '{key:"new_value"}')

    def test_delete_attribute(self):
        """
        This test checks that deleting an attribute from an NBT object
        updates the string representation accordingly.
        """
        
        nbt = NBT({"key": "value", "key2": "value2"})
        del nbt.key
        self.assertEqual(str(nbt), '{key2:"value2"}')

    def test_delete_attribute_error(self):
        """
        This test checks that trying to delete a non-existent
        attribute on an NBT object raises an AttributeError.
        """
        
        nbt = NBT()
        with self.assertRaises(AttributeError):
            del nbt.non_existent_key

    def test_nested_nbt_init(self):
        """
        This test checks that initializing an NBT object with nested NBT data
        results in the expected string representation.
        """
        
        nested_nbt_data = {"key": {"nested_key": "nested_value"}}
        nbt = NBT(nested_nbt_data)
        self.assertEqual(str(nbt), '{key:{nested_key:"nested_value"}}')

    def test_nested_nbt_set_attribute(self):
        """
        This test checks that setting a nested attribute on an NBT
        object works correctly and updates the string representation.
        """
        
        nbt = NBT()
        nbt.key = NBT({"nested_key": "nested_value"})
        self.assertEqual(str(nbt), '{key:{nested_key:"nested_value"}}')

    def test_nested_nbt_update_attribute(self):
        """
        This test checks that updating a nested attribute on an NBT
        object works correctly and updates the string representation.
        """
        
        nbt = NBT({"key": NBT({"nested_key": "nested_value"})})
        nbt.key.nested_key = "new_nested_value"
        self.assertEqual(str(nbt), '{key:{nested_key:"new_nested_value"}}')
    
if __name__ == "__main__":
    unittest.main()