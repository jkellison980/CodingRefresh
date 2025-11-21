'''
Race class to hold and organize abilities and such for different races

Jeremy Ellison
Nov. 18, 2025
'''

class Race:
    def __init__(self, ability_bonuses=None, traits=None):
        self.ability_bonuses = ability_bonuses or {}
        self.traits = traits or []


    def apply_to_character(self, character):
        for ability, bonus in self.ability_bonuses.items():
            character.abilities[ability].score += bonus
        
        for trait in self.traits:
            character.traits[trait] = True


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
    def __init__(self):
        super().__init__(
                ability_bonuses={"str": 1,"dex": 1,"con": 0,
                                "int": 0,"wis": 0,"cha":0},
                traits = [

                ]
            )

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
    def __init__(self):
        super().__init__(
            ability_bonuses={"str": 0,"dex": 2,"con": 0,
                            "int": 0,"wis": 0,"cha":0},
            traits = [
                "Darkvision",
                "Fey Ancestry",
                "Keen Senses"
                ]
        )


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
    def __init__(self):
        super().__init__(
                ability_bonuses={"str": 0,"dex": 0,"con": 2,
                                "int": 0,"wis": 0,"cha":0},
                traits = [
                    "Darkvision",
                    "Stoneskin"
                    ]
            )

