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
Ranger
'''
class Ranger(Character_class):
    abilities = ["pet"]
    feats = ["sniper"]


'''
Barbarian
'''
class Barbarian(Character_class):
    pass


'''
Cleric
'''
class Cleric(Character_class):
    pass


'''
Paladin
'''
class Paladin(Character_class):
    pass


'''
Monk
'''
class Monk(Character_class):
    pass


'''
Rogue
'''
class Rogue(Character_class):
    pass


'''
Wizard
'''
class Wizard(Character_class):
    pass


'''
Sorcerer
'''
class Sorcerer(Character_class):
    pass


'''
Druid
'''
class Druid(Character_class):
    pass


'''
Bard
'''
class Bard(Character_class):
    pass


'''
Warlock
'''
class Warlock(Character_class):
    abilities = ["eldritchblast"]
    feats = ["warmage"]
