'''
Create a class for a character in DND. 
Basically just create a cllass where i can initialize 
all stats/health/class/name as a start.

'''

class Character:

    def __init__(self,name, char_class=None,
                 age=None, race=None,
                 str_score=None, dex_score=None, con_score=None,
                 int_score=None, wis_score=None, charisma_score=None
                 ):
        self.name = name
        self.char_class = char_class
        self.set_age(age)
        self.race = race

        #Strength
        self._str_score = None
        self._str_modifier = None
        if str_score is not None:
            self.str_score = str_score
        
        #Dexterity
        self.dex_score = None
        self.con_score = None
        self.int_score = None
        self.wis_score = None
        self.charisma_score = None


    def set_class(self, char_class):
        #To Do: validate input from list of valid options
        self.char_class = char_class

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.age = age
    
    def set_race(self, race):
        #To Do: Validate input from list of valid options
        self.race = race

    def get_class(self):
        return self.char_class
    
    def get_age(self):
        return self.age
    
    def get_race(self):
        return self.race
    
    ##############################################
    ############### Ability Scores ###############
    ##############################################

    @str_score.setter
    def str_score(self, score):
        if score is not None and not isinstance(score, int):
            raise TypeError("Strength score must be an integer")
        self._str_score = score
        self.str_modifier = self.calculate_modifier(score)

    @property
    def str_score(self):
        return self._str_score
    
    @property
    def dex_modifier(self):
        return self._str_modifier
    
    @dex_score.setter
    def dex_score(self, score):
        if score is not None and not isinstance(score, int):
            raise TypeError("Dexterity score must be an integer")
        self._dex_score = score
        self._dex_modifier = self.calculate_modifier(score)

    @property
    def dex_score(self):
        return self._dex_score
    
    @property
    def dex_modifier(self):
        return self._dex_modifier
    
    ############################################################
    def set_dex_score(self, dex_score):
        if not isinstance(dex_score, int):
            raise TypeError("dexterity score must be an integer")
        self.dex_score = dex_score
        
    def set_con_score(self, con_score):
        if not isinstance(con_score, int):
            raise TypeError("constitution score must be an integer")
        self.con_score = con_score
        
    def set_int_score(self, int_score):
        if not isinstance(int_score, int):
            raise TypeError("intelligence score must be an integer")
        self.int_score = int_score
    
    def set_wis_score(self, wis_score):
        if not isinstance(wis_score, int):
            raise TypeError("wisdom score must be an integer")
        self.wis_score = wis_score
    
    def set_charisma_score(self, charisma_score):
        if not isinstance(charisma_score, int):
            raise TypeError("charisma score must be an integer")
        self.charisma_score = charisma_score
    
    
    
    def get_dex_score(self):
        return self.dex_score
    
    def get_charisma_score(self):
        return self.charisma_score
    
    def get_int_score(self):
        return self.int_score
    
    def get_wis_score(self):
        return self.wis_score
    
    def get_con_score(self):
        return self.con_score
    
    ##############################################
    ############### Static Methods ###############
    ##############################################
    @staticmethod
    def calculate_modifier(score):
        if score < 1 or score > 30:
            raise ValueError("Score needs to be an integer between 1 and 30.")
        
        return (score - 10) // 2
    
    def __str__(self):
        return f"{self.name}\n{self.race} | {self.char_class}\n{self.age}"
