#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")
    
    # waits for user input to aquire name and their age
    user_name = input("Please enter your name:")
    
    # waits for user input to obtain age
    user_age = input("How old are you?")

    # display the input back to the user.
    print("Hello " + user_name,"your IPv4 address is: " + user_input)
    
# this calls main
main()

