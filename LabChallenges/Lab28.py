#!/usr/bin/env python3

#Jacob Frank

#Lab28

def main():
    # Create variable called challenge
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

    #Displays the strings "eyes, goggles and nothing" in a prompt
    print(f'My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}')
    
    #Create a variable called trial
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    
   #Creates variables to be applied from the trial dictionary
    Trial_Eyes= trial[2]["goggles"]
    Trial_Goggles= trial[2]["eyes"]
    Trial_Nothing= trial[-1]

    #Displays the strings "eyes, goggles and nothing" from the trial dictionary
    print(f'My {Trial_Eyes}! The {Trial_Goggles} do {Trial_Nothing}')
   
   #Create a variable called nightmare
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    
    #Creates variables for the strings needed
    Eyes = nightmare[0]["user"]['name'].get("first")
    Goggles= nightmare[0]["kumquat"]
    Nothing = nightmare[0]["d"]

    #Displays the strings "eyes, goggles and nothing" from the dictionary and it's sub dictionaries
    print(f'My {Eyes}! The {Goggles} do {Nothing}! ')

main()

