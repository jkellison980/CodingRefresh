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
        self._dex_score = None
        self._dex_modifier = None
        if dex_score is not None:
            self.dex_score = dex_score
        
        #Constitution
        self._con_score = None
        self._con_modifier = None
        if con_score is not None:
            self.con_score = con_score

        #Intelligence
        self._int_score = None
        self._int_modifier = None
        if int_score is not None:
            self.int_score = int_score

        #Wisdom
        self._wis_score = None
        self._wis_modifier = None
        if wis_score is not None:
            self.wis_score = wis_score

        #Charisma
        self._charisma_score = None
        self._charisma_modifier = None
        if charisma_score is not None:
            self.charisma_score = charisma_score


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
    
    #Strength
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
    def str_modifier(self):
        return self._str_modifier
    
    #Dexterity
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
    
    #Constitution
    @con_score.setter
    def con_score(self, score):
        if score is not None and not isinstance(score, int):
            raise TypeError("Constitution score must be an integer")
        self._con_score = score
        self._con_modifier = self.calculate_modifier(score)

    @property
    def con_score(self):
        return self._con_score
    
    @property
    def con_modifier(self):
        return self._con_modifier
    
    #Intelligence
    @int_score.setter
    def int_score(self, score):
        if score is not None and not isinstance(score, int):
            raise TypeError("Intelligence score must be an integer")
        self._int_score = score
        self._int_modifier = self.calculate_modifier(score)

    @property
    def int_score(self):
        return self._int_score
    
    @property
    def int_modifier(self):
        return self._int_modifier
    
    #Wisdom
    @wis_score.setter
    def wis_score(self, score):
        if score is not None and not isinstance(score, int):
            raise TypeError("Wisdom score must be an integer")
        self._wis_score = score
        self._wis_modifier = self.calculate_modifier(score)

    @property
    def wis_score(self):
        return self._wis_score
    
    @property
    def wis_modifier(self):
        return self._wis_modifier
    
    #Charisma
    @charisma_score.setter
    def charisma_score(self, score):
        if score is not None and not isinstance(score, int):
            raise TypeError("Charisma score must be an integer")
        self._charisma_score = score
        self._charisma_modifier = self.calculate_modifier(score)

    @property
    def charisma_score(self):
        return self._charisma_score
    
    @property
    def charisma_modifier(self):
        return self._charisma_modifier
    ############################################################

    
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
