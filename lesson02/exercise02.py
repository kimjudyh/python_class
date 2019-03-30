# lesson 02 chapt 2, challenge 2
'''
“Write a program that allows a user to enter his or her two favorite foods.
(use variables)
The program should then print out the name of a new food by joining the
original food names together.”
'''

# initialize variables
food1 = "";
food2 = "";

# user input
food1 = input("Hi, tell me your two favorite foods.\n\
Type in your first favorite food:\n");
food2 = input("Type in your second favorite food:\n");
food1 = food1.replace(" ","");
food2 = food2.replace(" ","");

# disply results
print("Here's your new favorite food:\n" + food1.upper() + food2.upper());
