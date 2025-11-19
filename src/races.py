'''
Race class to hold and organize abilities and such for different races

Jeremy Ellison
Nov. 18, 2025
'''

class Race:
    ability_bonuses = []
    abilities = []

    def apply_to_character(self, character):
        for ability, bonus in self.ability_bonuses.items():
            character.abilities[ability].score += bonus
            character.abilities[ability].update_modifier()
        
        for ability in self.abilities:
            setattr(character, ability, True)


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
    ability_bonuses = {"str": 1,"dex": 1,"con": 0,
                       "int": 0,"wis": 1,"cha":0}
    abilities = []


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
    ability_bonuses = {"str": 0,"dex": 2,"con": 0,
                       "int": 1,"wis": 0,"cha":0}
    abilities = ["darkvision"]


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
    ability_bonuses = {"str": 1,"dex": 0,"con": 2,
                       "int": 0,"wis": 0,"cha":0}
    abilities = ["darkvision"]
