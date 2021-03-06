﻿#!/usr/bin/python3.6

# Guess My Number
#
# The computer picks a random number between 1 and 100.
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low or right on the money.
# Assignment: Modify the Guess My Number program so that the player
# has a limited number of guesses. If the player fails to guess in time,
# the program should display an appropriately chastising message


import random  


print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")
# modification:
max_guess = 9;      # maximum number of guesses allowed
print("You've only got", max_guess, "tries...");

# set the initial values
the_number = random.randint(1, 100)
#the_number = 5;
guess = int(input("Take a guess: "))
#tries = 1


# guessing loop
# modification: change to for loop to allow only max number of guesses

# loop from 1 to max_guess-1 (bc already took a guess above)
for i in range(1,max_guess,1):
    # guess too high
    if guess > the_number and guess <= 100:
        print("Too high...");
        # ask for new guess, tell number of guesses left
        askAgain = "You've got "+str(max_guess-i)+" tries left. Take a guess: \n";
        guess = int(input(askAgain));
    # guess too low
    elif guess < the_number and guess >= 1:
        print("Too low...");
        # ask for new guess, tell number of guesses left
        askAgain = "You've got "+str(max_guess-i)+" tries left. Take a guess: \n";
        guess = int(input(askAgain));
    # guess >100 or <1
    elif guess > 100 or guess < 1:
        print("Your guess is out of range! Guess between 1 and 100.");
        askAgain = "You've got "+str(max_guess-i)+" tries left. Take a guess: \n";
        guess = int(input(askAgain));
    # guess is correct
    elif guess == the_number:
        print("Yay you got it!");
        break;
    # just in case...
    else:
        print("wat?");
else:       # loop ran through, guesses weren't correct
    print("No more guesses! :(");

##while guess != the_number:
##    if guess > the_number:
##        print("Lower...")
##    else:
##        print("Higher...")
##            
##    guess = int(input("Take a guess: "))
##    tries += 1
##

##print("You guessed it!  The number was", the_number)
##print("And it only took you", tries, "tries!\n")
##  
##input("\n\nPress the enter key to exit.")
