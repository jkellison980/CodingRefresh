'''
Race class to hold and organize abilities and such for different races

Jeremy Ellison
Nov. 18, 2025
'''

class Race:
    def apply_stat_bonus(self, character):
        raise NotImplementedError("The individual race must impliment this function")


'''
Human Race
Stats
    STR +1

Abilities
    TBD

Feats

'''
class Human(Race):
    def apply_stat_bonus(self, character):
        character.str_score += 1


'''
Elf Race
Stats
    DEX +1

Abilities
    TBD

Feats

'''
class Elf(Race):
    def apply_stat_bonus(self, character):
        character.dex_score += 1