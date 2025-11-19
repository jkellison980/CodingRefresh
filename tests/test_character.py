#python3 -m unittest -v tests.test_character 
import unittest
from src import Ability
from src import Character
from src import Race, Human, Elf, Dwarf
from src import Character_class, Fighter, Warlock, Ranger

# ----------------------------------------
# Mock Race for Testing
# ----------------------------------------
class MockRace:
    """Simple test race that adds +2 STR and +1 DEX."""
    def apply_to_character(self, character):
        character.abilities["str"].base += 2
        character.abilities["dex"].base += 1


class CharacterTests(unittest.TestCase):

    # ---------- BASIC INIT TEST ----------
    def test_character_initialization(self):
        c = Character(
            name="Testy",
            str_base=15, dex_base=14, con_base=13,
            int_base=12, wis_base=10, cha_base=8
        )

        self.assertEqual(c.name, "Testy")
        self.assertEqual(c.str_score, 15)
        self.assertEqual(c.dex_score, 14)
        self.assertEqual(c.con_score, 13)
        self.assertEqual(c.int_score, 12)
        self.assertEqual(c.wis_score, 10)
        self.assertEqual(c.cha_score, 8)

    # ---------- ABILITY MODIFIER TEST ----------
    def test_modifiers(self):
        c = Character("ModTester", str_base=16)  # +3 mod
        
        self.assertEqual(c.str_modifier, 3)

        c.set_ability("str", 9)  # should become -1
        self.assertEqual(c.str_modifier, -1)

    # ---------- TEST RACE APPLICATION ----------
    def test_set_race(self):
        race = MockRace()
        c = Character("RaceTester", str_base=10, dex_base=10)

        c.set_race(race)

        # Race should modify the ability scores
        self.assertEqual(c.str_score, 12)
        self.assertEqual(c.dex_score, 11)
        self.assertIs(c.race, race)

    # ---------- CLASS SET/GET ----------
    def test_set_get_character_class(self):
        c = Character("Classy", character_class=Fighter())
        self.assertIsInstance(c.get_character_class(), Fighter)

        c.set_character_class(Warlock())
        self.assertIsInstance(c.get_character_class(), Warlock)


if __name__ == "__main__":
    unittest.main()