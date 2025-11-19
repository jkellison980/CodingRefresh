import unittest
from src import Ability

class TestAbility(unittest.TestCase):
    
    def test_initialization_defaults(self):
        # Default score should be 10
        a = Ability("Strength")
        self.assertEqual(a.score, 10)
        self.assertEqual(a.base, 10)
        self.assertEqual(a.modifier, 0)
    
    def test_initialization_custom_score(self):
        a = Ability("Dexterity", 14)
        self.assertEqual(a.score, 14)
        self.assertEqual(a.base, 14)
        self.assertEqual(a.modifier, 2)  # (14 - 10) // 2 = 2
    
    def test_score_setter_updates_modifier(self):
        a = Ability("Wisdom", 10)
        a.score = 16
        self.assertEqual(a.score, 16)
        self.assertEqual(a.modifier, 3)
        
        a.score = 9
        self.assertEqual(a.score, 9)
        self.assertEqual(a.modifier, -1)
    
    def test_base_setter_updates_score_and_modifier(self):
        a = Ability("Strength", 12)
        a.base = 14
        # score should increase by 2 automatically
        self.assertEqual(a.base, 14)
        self.assertEqual(a.score, 14)
        self.assertEqual(a.modifier, 2)
        
        a.base = 10
        self.assertEqual(a.base, 10)
        self.assertEqual(a.score, 10)
        self.assertEqual(a.modifier, 0)
    
    def test_score_limits(self):
        a = Ability("Constitution", 10)
        # Above 30 should cap modifier calculation
        a.score = 35
        self.assertEqual(a.modifier, (30 - 10) // 2)
        
        # Below 1 should raise ValueError
        with self.assertRaises(ValueError):
            a.calculate_modifier(0)

if __name__ == "__main__":
    unittest.main()
