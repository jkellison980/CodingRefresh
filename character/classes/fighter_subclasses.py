'''
Fighter Subclasses
'''

from .fighter import Fighter

class Champion(Fighter):
    feats = ["improved_critical"]

class BattleMaster(Fighter):
    feats = ["maneuvers"]

class EldritchKnight(Fighter):
    abilities = ["spellcasting"]