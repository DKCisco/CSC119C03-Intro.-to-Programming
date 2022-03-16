# Guess a number from 1 to 10
# By C. Calongne, 01/14/2019
# Pseudocode & Python with Iteration M3Lab1_student.py
# Guess a number from 1 to 10
# Write the statements requested in Steps 1-6 below
# 
# See the examples in the provided code
# Use structured programming and indent your code.
# Programmer Name: Dillan Craig

import random
from unicodedata import name

# uses randrange instead of randint for better results in Python 3.7 
# randrange stops just before the upper range, use (1, 11) for 1-10

num = random.randrange(1, 11)
# Step 1: Ask the player to enter a name or quit to exit
player_name = input("Enter your name or quit to exit. ") 



# Step 2: use a while statement to test when the name is not equal to quit
while (player_name != 'quit'):

    # Step 3: input enter a number from 1 to 10 for the variable your_guess
    your_guess = int(input("Enter a number from 1 to 10: "))
    # display the number guessed
    print("Your number is", your_guess)

    while num != your_guess:

        # Step 4: Write an if statement for your_guess is less than num
            if your_guess < num:

                print("Your guess is too low.")
                your_guess = int(input("Guess another number from 1 to 10: "))

            elif your_guess > num:
                print("Your guess is too high")
            your_guess = int(input("Guess another number from 1 to 10: "))

    else:

        print("The correct number was", num)
        # Step 5 display text with your guess and You won, name
        print("Your guess of ", your_guess, "was correct! Congrats", player_name, "you have won!")


    print("***************************************************************")
    # Step 6 ask the player to enter a name or quit to exit
    player_name = input("Enter your name. ")

    num = random.randrange(1, 11)
print("Thank you for playing!") 


