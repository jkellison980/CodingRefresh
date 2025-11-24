'''
This is the Character object. This object holds information pertaining to a character in DnD, 
things like the character's stats, race, class, etc. These stats can be pulled at any time and any related 
modifiers are automatically updated.

Jeremy Ellison
Nov. 17, 2025

'''
from .ability import Ability
from .races import Race #not technically needed at present, but could be useful later on
class Character:

    def __init__(self,name, character_class=None, race=None,
                 str_base=10, dex_base=10, con_base=10,
                 int_base=10, wis_base=10, cha_base=10
                 ):
        #Base Ability scores
        self.abilities = {
            "str": Ability("Strength", str_base),
            "dex": Ability("Dexterity", dex_base),
            "con": Ability("Constitution", con_base),
            "int": Ability("Intelligence", int_base),
            "wis": Ability("Wisdom", wis_base),
            "cha": Ability("Charisma", cha_base),
        }
        
        #Traits
        self.traits = {}

        self.name = name
        self.character_class = None
        if character_class:
            self.set_character_class(character_class)

        #Race
        self.race = None
        if race:
            self.set_race(race)


# ---------------- MANAGE RACE ----------------
    def set_race(self, race_obj):
        self.race = race_obj
        race_obj.apply_to_character(self)
    
    def get_race(self):
        return self.race

# ---------------- MANAGE CLASS ----------------
    def set_character_class(self, character_class_object):
        self.character_class = character_class_object
        character_class_object.apply_to_character(self)

    def get_character_class(self):
        return self.character_class

# ---------------- ABILITY SCORES ----------------
    def set_ability(self,key:str,new_value:int):
        self.abilities[key].base = new_value
        
    @property
    def str_score(self):
        return self.abilities["str"].score
    
    @property
    def dex_score(self):
        return self.abilities["dex"].score
    
    @property
    def con_score(self):
        return self.abilities["con"].score
    
    @property
    def int_score(self):
        return self.abilities["int"].score
    
    @property
    def wis_score(self):
        return self.abilities["wis"].score
    
    @property
    def cha_score(self):
        return self.abilities["cha"].score
    
# ---------------- MODIFIER GETTERS ----------------
    @property
    def str_modifier(self):
        return self.abilities["str"].modifier
    
    @property
    def dex_modifier(self):
        return self.abilities["dex"].modifier
    
    @property
    def con_modifier(self):
        return self.abilities["con"].modifier
    
    @property
    def int_modifier(self):
        return self.abilities["int"].modifier
    
    @property
    def wis_modifier(self):
        return self.abilities["wis"].modifier
    
    @property
    def cha_modifier(self):
        return self.abilities["cha"].modifier
    
# ---------------- STRING FORMATTER ----------------

    def __str__(self):
        
        def fmt_mod(value):
            return f"{value:+d}"

        abilities_str = "\n".join(
            f"  {ability_obj.name:<12} {ability_obj.score:>2}  ({fmt_mod(ability_obj.modifier)})"
            for key, ability_obj in self.abilities.items()
        )

        traits_str = "\n".join(
            f"  {trait}" for trait in self.traits
        )

        race_name = self.race.__class__.__name__ if self.race else "None"
        class_name = self.character_class.__class__.__name__ if self.character_class else "None"

        return (
            f"Character Sheet\n"
            f"-----------------------------\n"
            f"Name: {self.name}\n"
            f"Race: {race_name}\n"
            f"Class: {class_name}\n\n"
            f"Abilities:\n{abilities_str}\n\n"
            f"Traits: \n{traits_str}"
        )
