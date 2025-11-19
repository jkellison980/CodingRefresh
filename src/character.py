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

    def __init__(self,name, char_class=None, race=None,
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

        self.name = name
        self.char_class = char_class #will need to update to resemble race once options are available

        #Race
        self.race = None
        if race:
            self.set_race(race)


# ---------------- MANAGE RACE ----------------
    def set_race(self, race_obj):
        self.race = race_obj
        race_obj.apply_to_character(self)


#    def set_race(self, race):
#        #remove old race effects
#        if self.race:
#            self.race.remove_effects(self)
#        
#        #apply new race
#        self.race = race
#        self.race.apply_effects(self)

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
    

# ------------------------------------------------
    def set_class(self, char_class):
        #To Do: validate input from list of valid options
        self.char_class = char_class

    def get_class(self):
        return self.char_class
    

    