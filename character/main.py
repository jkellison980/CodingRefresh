from character import Ability
from character import Character
from character import Race, Human, Elf, Dwarf
from character import Character_class, Fighter, Warlock, Ranger

name = "Jeremy"

char1 = Character(
    name=name,
    character_class=Fighter(),
    race=Human()
)
char2 = Character(
    name=name,
    character_class=Warlock(),
    race=Elf()
)

print(char1)
print(char2)
