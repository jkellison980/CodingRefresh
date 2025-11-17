import unittest
from src.character import Character 


class TestCharacter(unittest.TestCase):

    def test_initialization(self):
        char = Character("Aragorn", char_class="Ranger", age=87, race="Human")
        self.assertEqual(char.name, "Aragorn")
        self.assertEqual(char.get_class(), "Ranger")
        self.assertEqual(char.get_age(), 87)
        self.assertEqual(char.get_race(), "Human")

    def test_setters(self):
        char = Character("Legolas")
        char.set_class("Archer")
        char.set_age(2931)
        char.set_race("Elf")

        self.assertEqual(char.get_class(), "Archer")
        self.assertEqual(char.get_age(), 2931)
        self.assertEqual(char.get_race(), "Elf")

    def test_getters_with_initial_none(self):
        char = Character("Gimli")
        self.assertIsNone(char.get_class())
        self.assertIsNone(char.get_age())
        self.assertIsNone(char.get_race())

    def test_str_representation(self):
        char = Character("Frodo", char_class="Ringbearer", age=50, race="Hobbit")
        expected_str = "Frodo\nHobbit | Ringbearer\n50"
        self.assertEqual(str(char), expected_str)

    def test_partial_initialization(self):
        # Only name given, others default to None
        char = Character("Boromir")
        self.assertEqual(char.name, "Boromir")
        self.assertIsNone(char.get_class())
        self.assertIsNone(char.get_age())
        self.assertIsNone(char.get_race())


if __name__ == "__main__":
    unittest.main()
