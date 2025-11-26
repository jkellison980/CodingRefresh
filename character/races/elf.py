'''
Elf Race
Stats
    DEX +2

Abilities
    TBD

Feats
    TBD
'''

from .race import Race

class Elf(Race):
    NAME = "Elf"
    ABILITY_BONUSES = {"dex": 2}
    TRAITS = [
        "Darkvision",
        "Fey Ancestry",
        "Keen Senses"
        ]

    def __init__(self):
        super().__init__(
                ability_bonuses=self.ABILITY_BONUSES,
                traits = self.TRAITS
            )
