'''
Dwarf Race
Stats
    CON +2

Abilities
    TBD

Feats
    TBD
'''

from .race import Race

class Dwarf(Race):
    NAME = "Dwarf"
    ABILITY_BONUSES = {"con": 2}
    TRAITS = [
        "Darkvision",
        "Stoneskin"
        ]

    def __init__(self):
        super().__init__(
                ability_bonuses=self.ABILITY_BONUSES,
                traits = self.TRAITS
            )
