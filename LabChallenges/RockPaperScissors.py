#!/usr/bin/env python3

import random

# Lists variables for the list

Options = ['Rock', "Paper", "Scissors"]
Opponent_str = random.choice(Options)

user_Option = input(f"Please select an option out of the three provded. \n"
        "Rock, Paper or Scissors: ")

if user_Option  == 'Rock' and Opponent_str == 'Paper':
    print('You win!')
elif user_Option == 'Rock' and Opponent_str == 'Scissors':
    print('Sorry, you lose')
elif user_Option == 'Rock' and Opponent_str == 'Rock':
    print('It is a draw!')
elif user_Option == 'Paper' and Opponent_str == 'Rock':
    print('You win!')
elif user_Option == 'Paper' and Opponent_str == 'Scissors':
    print('Sorry, you lose')
elif user_Option == 'Paper' and Opponent_str == 'Paper':
    print('It is a draw!')
elif user_Option == 'Scissors' and Opponent_str == 'Paper':
    print('You win!')
elif user_Option == 'Scissors' and Opponent_str == 'Rock':
    print('Sorry, you lose')
elif user_Option == 'Scissors' and Opponent_str == 'Scissors':
    print('Its is a draw!')
