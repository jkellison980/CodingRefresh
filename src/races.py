'''
Race class to hold and organize abilities and such for different races

Jeremy Ellison
Nov. 18, 2025
'''

class Race:
    def apply_effects(self, character):
        raise NotImplementedError("The individual race must impliment this function")
    
    def remove_effects(self, character):
        raise NotImplementedError("The individual race must impliment this function")


'''
Human Race
Stats
    STR +1
    DEX +1
    WIS +1

Abilities
    TBD

Feats
    TBD
'''
class Human(Race):
    def apply_effects(self, character):
        character.str_score += 1
        character.dex_score += 1
        character.wis_score += 1
    
    def remove_effects(self, character):
        character.str_score -= 1
        character.dex_score -= 1
        character.wis_score -= 1


'''
Elf Race
Stats
    DEX +2
    INT +1

Abilities
    TBD

Feats
    TBD
'''
class Elf(Race):
    def apply_effects(self, character):
        character.dex_score += 2
        character.int_score += 1

    def remove_effects(self, character):
        character.dex_score -= 2
        character.int_score -= 1


'''
Dwarf Race
Stats
    STR +1
    CON +2

Abilities
    TBD

Feats
    TBD
'''
class Dwarf(Race):
    def apply_effects(self, character):
        character.str_score += 1
        character.con_score += 1
    
    def remove_effects(self, character):
        character.str_score -= 1
        character.con_score -= 1