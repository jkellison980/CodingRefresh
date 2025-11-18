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
    bonuses = {
        "str_score": 1,
        "dex_score": 1,
        "wis_score": 1
    }
    abilities = {}

    def apply_effects(self, character):
        for stat, value in self.bonuses.items():
            character.add_modifier(stat, value, source="Human")
        for ability, value in self.abilities.items():
            character.add_ability(ability, value, source="Human")
    
    def remove_effects(self, character):
        character.remove_modifiers_from_source("Human")
        character.remove_abilities_from_source("Human")


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
    bonuses = {
        "dex_score": 2,
        "int_score": 1
    }
    abilities = {
        "darkvision": True
    }

    def apply_effects(self, character):
        for stat, value in self.bonuses.items():
            character.add_modifier(stat, value, source="Elf")
        for ability, value in self.abilities.items():
            character.add_ability(ability, value, source="Elf")
    
    def remove_effects(self, character):
        character.remove_modifiers_from_source("Elf")
        character.remove_abilities_from_source("Elf")


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
    bonuses = {
        "con_score": 2,
        "str_score": 1
    }
    abilities = {
        "darkvision": True
    }

    def apply_effects(self, character):
        for stat, value in self.bonuses.items():
            character.add_modifier(stat, value, source="Dwarf")
        for ability, value in self.abilities.items():
            character.add_ability(ability, value, source="Dwarf")
    
    def remove_effects(self, character):
        character.remove_modifiers_from_source("Dwarf")
        character.remove_abilities_from_source("Dwarf")