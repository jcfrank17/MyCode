#!/usr/bin/env python3

#Jacob Frank

#Lab21

print('Script is running')

def main():
    #creating list called wordbank
    wordbank = ["indentation", "spaces"]
    
    #createing list called tlg students
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    
    #Appending wordbank to add the number 4
    wordbank.append('4')
    
    #Asks for input from the user for a number between 0-20
    user_numberStr = input('Select a student number between 0-20: ')

    user_numberInt = int(user_numberStr)

    #Number from user will slice the list of students

    Student = tlgstudents[user_numberInt]

    #Will print the outcome of the script

    print(f'{Student} always uses {wordbank[1]} {wordbank[2]} to indent.')

    print('Script is done running')
main()

