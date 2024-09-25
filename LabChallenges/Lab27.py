#!/usr/bin/env python3

#Jacob Frank

def main():
    
    # Create Dictionaries for the 3 marvel characters
    MarvelChar= {
            "Starlord": #Creates first entry in the Marvel Characters variable
            {"Real name": "Peter Quill",
            "Powers": "Dance moves",
            "Archenemy": "Thanos"},
            "Mystique" : #Creates Second entry in the Marvel Characters variable
            {"Real name": "Raven Darkholme",
            "Powers": "Shape shifter",
            "Archenemy": "Professor X"},
            "Hulk": # Creates the third entry in the Marvel Characters variable
            {"Real name": "Bruce Banner",
            "Powers": "Super strength",
            "Archenemy": "Adrenaline"}
            }
    # Prompt the user for their input for char_name
    char_name = input("Which marvel character would you like to know more about? (Starlord, Mystique or Hulk) \n")
    
    #Ecapsulates the selected name from the user
    Selected_name = MarvelChar.get(char_name)
    
    #Prompt the user for the stat for the name selected name
    char_stat = input("Great, now what about their stat? (Real name, Powers or Archenemy? \n")
    
    #Assign the input to be Selected_stat and called in the print feature
    Selected_stat = Selected_name.get(char_stat)

    # Will print out the end result
    print(f"{char_name}'s {char_stat} is {Selected_stat}.")

main()
