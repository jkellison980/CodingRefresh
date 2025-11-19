import unittest
from src import Ability
from src import Character
from src import Race, Human, Elf, Dwarf

class DummyCharacter(Character):
    """A minimal Character class for testing Race."""
    def __init__(self):
        # Create a simple abilities dict with Ability objects
        self.abilities = {key: Ability(key) for key in ["str","dex","con","int","wis","cha"]}
        # Placeholder for any boolean abilities
        self.darkvision = False

class TestRaces(unittest.TestCase):

    def setUp(self):
        self.char = DummyCharacter()

    def test_human_ability_bonuses(self):
        human = Human()
        human.apply_to_character(self.char)
        # Test ability scores
        self.assertEqual(self.char.abilities["str"].score, 11)
        self.assertEqual(self.char.abilities["dex"].score, 11)
        self.assertEqual(self.char.abilities["wis"].score, 11)
        self.assertEqual(self.char.abilities["con"].score, 10)
        # Test modifiers updated
        self.assertEqual(self.char.abilities["str"].modifier, 0)
        self.assertEqual(self.char.abilities["dex"].modifier, 0)
        self.assertEqual(self.char.abilities["wis"].modifier, 0)

    def test_elf_ability_bonuses_and_abilities(self):
        elf = Elf()
        elf.apply_to_character(self.char)
        # Test ability scores
        self.assertEqual(self.char.abilities["dex"].score, 12)
        self.assertEqual(self.char.abilities["int"].score, 11)
        self.assertEqual(self.char.abilities["str"].score, 10)
        # Test modifier updated
        self.assertEqual(self.char.abilities["dex"].modifier, 1)
        self.assertEqual(self.char.abilities["int"].modifier, 0)
        # Test special ability applied
        self.assertTrue(self.char.darkvision)

    def test_dwarf_ability_bonuses_and_abilities(self):
        dwarf = Dwarf()
        dwarf.apply_to_character(self.char)
        # Test ability scores
        self.assertEqual(self.char.abilities["str"].score, 11)
        self.assertEqual(self.char.abilities["con"].score, 12)
        self.assertEqual(self.char.abilities["dex"].score, 10)
        # Test modifier updated
        self.assertEqual(self.char.abilities["str"].modifier, 0)
        self.assertEqual(self.char.abilities["con"].modifier, 1)
        # Test special ability applied
        self.assertTrue(self.char.darkvision)

if __name__ == "__main__":
    unittest.main()
