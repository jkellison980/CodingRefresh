from src import Ability
from src import Character
from src import Race, Human, Elf, Dwarf
from src import Character_class, Fighter, Warlock, Ranger

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
