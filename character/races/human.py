'''
Human Race
Stats
    STR +1
    DEX +1

Abilities
    TBD

Feats
    TBD
'''

from .race import Race


class Human(Race):
    NAME = "Human"
    ABILITY_BONUSES = {"str": 1,"dex": 1}
    TRAITS = []

    def __init__(self):
        super().__init__(
                ability_bonuses=self.ABILITY_BONUSES,
                traits = self.TRAITS
            )
