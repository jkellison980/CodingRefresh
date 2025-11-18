'''
This is the Character object. This object holds information pertaining to a character in DnD, 
things like the character's stats, race, class, etc. These stats can be pulled at any time and any related 
modifiers are automatically updated.

Jeremy Ellison
Nov. 17, 2025

'''

class Character:

    def __init__(self,name, char_class=None,
                 age=None, race=None,
                 str_base=None, dex_base=None, con_base=None,
                 int_base=None, wis_base=None, cha_base=None
                 ):
        #Base Ability scores
        self.base_str = str_base or 10
        self.base_dex = dex_base or 10
        self.base_con = con_base or 10
        self.base_int = int_base or 10
        self.base_wis = wis_base or 10
        self.base_cha = cha_base or 10
        
        self.modifiers = {}
        self.abilities = {}
        self.name = name
        self.char_class = char_class #will need to update to resemble race once options are available
        self.set_age(age)

        #Race
        self.race = None
        if race:
            race.set_race(self)

# ---------------- MODIFIER API ----------------
    def add_modifier(self, stat, value, source):
        self.modifiers.setdefault(stat, [])
        self.modifiers[stat].append({"value": value, "source": source})

    def remove_modifiers_from_source(self, source):
        for stat in list(self.modifiers.keys()):
            self.modifiers[stat] = [
                m for m in self.modifiers[stat] if m["source"] != source
            ]
            if not self.modifiers[stat]:
                del self.modifiers[stat]

# ---------------- ABILITY API ----------------
    def add_ability(self, name, value, source):
        self.abilities[name] = {"value": value, "source": source}

    def remove_abilities_from_source(self, source):
        for name in list(self.abilities.keys()):
            if self.abilities[name]["source"] == source:
                del self.abilities[name]

# ---------------- MANAGE RACE ----------------
    def set_race(self, race):
        #remove old race effects
        if self.race:
            self.race.remove_effects(self)
        
        #apply new race
        self.race = race
        self.race.apply_effects(self)

# ---------------- ABILITY SCORES ----------------

    @property
    def str_score(self):
        total = self.base_str
        for x in self.modifiers.get("str_score", []):
            total += x["value"]
        return total
    
    @property
    def dex_score(self):
        total = self.base_dex
        for x in self.modifiers.get("dex_score", []):
            total += x["value"]
        return total
    
    @property
    def con_score(self):
        total = self.base_con
        for x in self.modifiers.get("con_score", []):
            total += x["value"]
        return total
    
    @property
    def int_score(self):
        total = self.base_int
        for x in self.modifiers.get("int_score", []):
            total += x["value"]
        return total
    
    @property
    def wis_score(self):
        total = self.base_wis
        for x in self.modifiers.get("wis_score", []):
            total += x["value"]
        return total
    
    @property
    def cha_score(self):
        total = self.base_cha
        for x in self.modifiers.get("cha_score", []):
            total += x["value"]
        return total
    
# ---------------- MODIFIER CALCULATION ----------------
    @staticmethod
    def calculate_modifier(score):
        if score < 1:
            raise ValueError("Score needs to be an integer above 1")
        if score > 30:
            score = 30
        
        return (score - 10) // 2

    #Ability Modifiers
    @property
    def str_modifier(self):
        return Character.calculate_modifier(self.str_score)
    
    @property
    def dex_modifier(self):
        return Character.calculate_modifier(self.dex_score)
    
    @property
    def con_modifier(self):
        return Character.calculate_modifier(self.con_score)
    
    @property
    def int_modifier(self):
        return Character.calculate_modifier(self.int_score)
    
    @property
    def wis_modifier(self):
        return Character.calculate_modifier(self.wis_score)
    
    @property
    def cha_modifier(self):
        return Character.calculate_modifier(self.cha_score)
    

# ------------------------------------------------
    def set_class(self, char_class):
        #To Do: validate input from list of valid options
        self.char_class = char_class

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.age = age

    def get_class(self):
        return self.char_class
    
    def get_age(self):
        return self.age
    