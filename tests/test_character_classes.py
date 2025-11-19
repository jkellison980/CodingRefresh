import unittest
from src import Ability
from src import Character
from src import Race, Human, Elf, Dwarf
from src import Character_class, Fighter, Warlock, Ranger

class DummyCharacter(Character):
    """A minimal Character class for testing Character_class."""
    def __init__(self):
        # Create a simple abilities dict with Ability objects
        self.abilities = {key: Ability(key) for key in ["str","dex","con","int","wis","cha"]}
        # Boolean abilities do not need prior placeholders, they are instantiated upon calling

class TestCharacterClasses(unittest.TestCase):

    def setUp(self):
        self.char = DummyCharacter()

    def test_fighter_feats_and_abilities(self):
        fighter = Fighter()
        fighter.apply_to_character(self.char)
        # Test special ability applied
        self.assertTrue(self.char.swingsword)
        self.assertTrue(self.char.sentinal)

    def test_warlock_feats_and_abilities(self):
        warlock = Warlock()
        warlock.apply_to_character(self.char)
        # Test special ability applied
        self.assertTrue(self.char.eldritchblast)
        self.assertTrue(self.char.warmage)

    def test_ranger_feats_and_abilities(self):
        ranger = Ranger()
        ranger.apply_to_character(self.char)
        # Test special ability applied
        self.assertTrue(self.char.pet)
        self.assertTrue(self.char.sniper)

if __name__ == "__main__":
    unittest.main()
