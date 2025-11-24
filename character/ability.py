'''
Organize the ability scores of character.
'''

class Ability:
    def __init__(self, name, score=10):
        self.name = name
        self._score = score
        self._base = score
        self.modifier = self.calculate_modifier(self._score)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        self._score = new_score
        self.modifier = self.calculate_modifier(self._score)

    def calculate_modifier(self, score):
        if score < 1:
            raise ValueError("Score needs to be an integer above 1")
        if score > 30:
            score = 30
        
        return (score - 10) // 2

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, new_base):
        difference = new_base - self._base
        self._base = new_base
        if difference != 0:
            self.score += difference
