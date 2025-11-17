'''
Create a class for a character in DND. 
Basically just create a cllass where i can initialize 
all stats/health/class/name as a start.

'''

class Character:

    def __init__(self,name, char_class=None,
                 age=None, race=None):
        self.name = name
        self.char_class = char_class
        self.age = age
        self.race = race

    def set_class(self, char_class):
        self.char_class = char_class

    def set_age(self, age):
        self.age = age
    
    def set_race(self, race):
        self.race = race

    def get_class(self):
        return self.char_class
    
    def get_age(self):
        return self.age
    
    def get_race(self):
        return self.race
    
    def __str__(self):
        return f"{self.name}\n{self.race} | {self.char_class}\n{self.age}"
