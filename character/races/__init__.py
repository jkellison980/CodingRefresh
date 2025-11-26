#character/races
#from .<filename> import <class>
from .elf import Elf
from .dwarf import Dwarf
from .human import Human
#from .elf_subclasses import HighElf, WoodElf

__all__ = [
    "Elf",
    "Dwarf",
    "Human"
]
