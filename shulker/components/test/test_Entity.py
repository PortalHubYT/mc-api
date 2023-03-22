import unittest

from shulker.components.Entity import Entity, NBT, generate_signed_32bit_integer_uuid_list, entities_nbt

class TestEntity(unittest.TestCase):

    def test_invalid_entity(self):
        """
        This test checks whether the Entity class raises a ValueError
        when trying to create an instance with an invalid entity name.
        """
        
        with self.assertRaises(ValueError):
            Entity("invalid_entity")

    def test_valid_entity(self):
        """
        This test checks whether the Entity class can create a valid
        instance with a valid entity name, and ensures the descriptor
        is correctly assigned.
        Additionally, it checks whether a mispell in the entity name
        is correcter by the Entity class.
        """
        
        entity = Entity("Zombie")
        self.assertEqual(entity.descriptor, "zombie")

    def test_nbt_type(self):
        """
        This test checks whether the Entity class raises a ValueError
        when trying to create an instance with an invalid nbt input type.
        """
        
        with self.assertRaises(ValueError):
            Entity("zombie", nbt="invalid_nbt_type")

    def test_valid_nbt(self):
        """
        This test checks whether the Entity class can create a valid
        instance with a valid NBT object input, and ensures that
        the NBT values are correctly assigned.
        """
        
        entity = Entity("zombie", nbt=NBT({"CustomName": "zombie1"}))
        self.assertEqual(entity.CustomName, '"zombie1"')

    def test_dict_nbt(self):
        """
        This test checks whether the Entity class can create a valid
        instance with a valid dictionary input for nbt, and ensures
        that the NBT values are correctly assigned.
        """
        
        entity = Entity("zombie", nbt={"CustomName": "zombie2"})
        self.assertEqual(entity.CustomName, '"zombie2"')

    def test_set_nonexistent_attribute(self):
        """
        This test checks whether the Entity class
        raises a ValueError when trying to set a nonexistent
        attribute to an instance.
        """
        
        entity = Entity("zombie")
        with self.assertRaises(ValueError):
            entity.invalid_attribute = "value"

    def test_set_valid_attribute(self):
        """
        This test checks whether the Entity class can set a valid
        attribute for an instance, and ensures that the attribute
        value is correctly assigned.
        """
        
        entity = Entity("zombie")
        entity.Health = 20
        self.assertEqual(entity.Health, '20')

    def test_uuid_creation(self):
        """
        This test checks whether the Entity class generates a UUID
        for each instance and ensures that the UUID is a list of
        4 signed 32-bit integers.
        """
        import re

        entity = Entity("zombie")
        uuid_str = entity.UUID
        uuid_list = [int(num) for num in re.findall(r'-?\d+', uuid_str)]
        self.assertEqual(len(uuid_list), 4)
        for i in uuid_list:
            self.assertTrue(isinstance(i, int))

    def test_str_representation(self):
        """
        This test checks whether the __str__ method of the Entity class
        returns a string representation of the entity.
        """
        
        entity = Entity("zombie")
        self.assertTrue(isinstance(entity.__str__(), str))
        
    def test_attributes_property(self):
        entity = Entity("zombie")
        expected_attributes = entities_nbt["zombie"]
        self.assertEqual(entity.attributes, expected_attributes)

