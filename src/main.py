import reference_functions as rf
import character


name = "Jeremy"
race = "Tiefling"
race2 = "Human"
char_class = "Fighter"
char_class2 = "Ranger"
age = 23
age2 = 33

char1 = character.Character(name,char_class,age,race)
print (f"{char1}")