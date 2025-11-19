'''
Character_class holds an identifier for each class. Modelled initially after Race layout.

Jeremy Ellison
Nov. 19, 2025
'''

class Character_class:
    abilities = []
    feats = []

    def apply_to_character(self, character):
        for ability in self.abilities:
            setattr(character, ability, True)
        
        for feature in self.feats:
            setattr(character, feature, True)


'''
Fighter


'''
class Fighter(Character_class):
    abilities = ["swingsword"]
    feats = ["sentinal"]


'''
Warlock


'''
class Warlock(Character_class):
    abilities = ["eldritchblast"]
    feats = ["warmage"]


'''
Ranger


'''
class Ranger(Character_class):
    abilities = ["pet"]
    feats = ["sniper"]
