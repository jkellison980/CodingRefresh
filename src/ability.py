'''
Organize the ability scores of character.
'''

class Ability:
    def __init__(self, name, score=10):
        self.name = name
        self.score = score
        self.modifier = self.calculate_modifier(score)

    def calculate_modifier(self, score):
        if score < 1:
            raise ValueError("Score needs to be an integer above 1")
        if score > 30:
            score = 30
        
        return (score - 10) // 2
    
    def update_modifier(self):
        self.modifier = self.calculate_modifier(self.score)