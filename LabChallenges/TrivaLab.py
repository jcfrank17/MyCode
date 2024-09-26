#!/usr/bin/env python3

import html 

# Sets the dictionary as trivia
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
# Setting some variables and clean html
question= trivia["question"]
correct= html.unescape(trivia["correct_answer"])
incorrect1= html.unescape(trivia["incorrect_answers"][0])
incorrect2= html.unescape(trivia["incorrect_answers"][1])
incorrect3= html.unescape(trivia["incorrect_answers"][2])

# Print Question and Possible options
print(question)
print(f"A. {correct}")
print(f"B. {incorrect1}")
print(f"C. {incorrect2}")
print(f"D. {incorrect3}")

# Asks user for input
user_input = input("Choose the correct answer: ")

# Checks inputed Letter against the following IF statement
if user_input == "A":
    print("You are correct!")
elif user_input == "B":
    print("You're incorrect!")
elif user_input == "C":
    print("You're incorrect!")
elif user_input == "D":
    print("You're incorrect!")
