'''
Base class for specific character classes
'''

class CharacterClass:
    abilities = []
    feats = []

    def apply_to_character(self, character):
        for ability in self.abilities:
            setattr(character, ability, True)
        
        for feature in self.feats:
            setattr(character, feature, True)