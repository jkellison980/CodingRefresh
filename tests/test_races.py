import unittest
from src import Ability
from src import Character
from src import Race, Human, Elf, Dwarf

class TestRaces(unittest.TestCase):

    def setUp(self):
        self.char = Character(name="TestChar",
                              str_base=10,dex_base=10,con_base=10,
                              int_base=10,wis_base=10,cha_base=10
    )

    def test_human_ability_bonuses(self):
        human = Human()
        human.apply_to_character(self.char)
        # Test ability scores
        self.assertEqual(self.char.abilities["str"].score, 11)
        self.assertEqual(self.char.abilities["dex"].score, 11)
        self.assertEqual(self.char.abilities["wis"].score, 10)
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
        self.assertEqual(self.char.abilities["int"].score, 10)
        self.assertEqual(self.char.abilities["str"].score, 10)
        # Test modifier updated
        self.assertEqual(self.char.abilities["dex"].modifier, 1)
        self.assertEqual(self.char.abilities["int"].modifier, 0)
        # Test special ability applied
        self.assertTrue(self.char.traits["Darkvision"])

    def test_dwarf_ability_bonuses_and_abilities(self):
        dwarf = Dwarf()
        dwarf.apply_to_character(self.char)
        # Test ability scores
        self.assertEqual(self.char.abilities["str"].score, 10)
        self.assertEqual(self.char.abilities["con"].score, 12)
        self.assertEqual(self.char.abilities["dex"].score, 10)
        # Test modifier updated
        self.assertEqual(self.char.abilities["str"].modifier, 0)
        self.assertEqual(self.char.abilities["con"].modifier, 1)
        # Test special ability applied
        self.assertTrue(self.char.traits["Darkvision"])
    
    def test_get_race(self):
        dwarf = Dwarf()
        human = Human()
        elf = Elf()

        # check initial state
        self.assertIsNone(self.char.get_race())

        # Apply Dwarf Race and test
        self.char.set_race(dwarf)
        self.assertEqual(self.char.get_race(), dwarf)
        self.assertIsInstance(self.char.get_race(), Dwarf)

        # Apply human race and test
        self.char.set_race(human)
        self.assertEqual(self.char.get_race(), human)
        self.assertIsInstance(self.char.get_race(), Human)

        # Apply elf race and test
        self.char.set_race(elf)
        self.assertEqual(self.char.get_race(), elf)
        self.assertIsInstance(self.char.get_race(), Elf)

if __name__ == "__main__":
    unittest.main()
