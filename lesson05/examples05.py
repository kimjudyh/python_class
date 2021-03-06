﻿#######################################################################################################################
'''
Examples of Python Code Samples; examples.py
Contents:
  Lesson 01 - Print and Input commands
  Lesson 02 - Strings, variables
  Lesson 03 - Numeric data types, Operators, Type conversion, String methods
  Lesson 04 - Importing Modules, Conditions, Conditional branching, code blocks
  Lesson 05 - while loop, option menu, indexes
'''




#######################################################################################################################
## Lesson 05
# ----------------------
# While loop
# ----------------------
vi_count = 10;                  # Initialize loop variable
while vi_count > 0:             # Check loop variable
    vi_count = vi_count -1;     # Update loop variable
    print(vi_count, end=" ");
print("\n End of Count!");




# ----------------------
# Option Menu with while loop and conditional branching
# There is a logic error in the conditional branching for 'x'
# How should it be fixed?
# ----------------------
vs_choice = '';                 # Initialize the option choice loop variable
while vs_choice != 'x': # Check loop variable
    print("\nChoose a color for your new car"); 
    print(" 1. Red    ");
    print(" 2. Green  ");
    print(" 3. Yellow ");
    print(" 4. Blue   ");
    print(" x. Exit   ");


  # Get menu choice - Update loop variable
    vs_choice = input("\nEnter the number for your choice of color: "); 


    if   vs_choice == '1':
       print("You chose Red    ");
       
    elif vs_choice == '2':
       print("You chose Green  ");
       
    elif vs_choice == '3':
       print("You chose Yellow ");
       
    elif vs_choice == '4':
       print("You chose Blue   ");
       
    elif vs_choice == 'x':
       print("You chose Exit   ");
       
    else:
       print("\nThat is not a valid choice");


# End of while loop








# ----------------------
# Indexing
# ----------------------
'''
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5
 -6  -5  -4  -3  -2  -1 
'''
str = 'Python';  # Initialize string variable


# Print the string sequence: character by character forward
index = 0;                            # Initialize loop variable
while index < len(str):               # Check loop variable
     print (str[index], end = "-");   # print character at index
     index +=1;                       # Update loop variable
print();






#######################################################################################################################
## Lesson 04
# ----------------------
# Assignment 1 - Importing modules
# ----------------------
import random;
rand_nbr = random.randint(1, 6); print(rand_nbr); # randint 1-6 inclusive
rand_nbr = random.randrange(6);  print(rand_nbr); # randrange 0-5


from random import randint, randrange;
rand_nbr = randint(1, 6); print(rand_nbr); # randint 1-6 inclusive
rand_nbr = randrange(6);  print(rand_nbr); # randrange 0-5




# ----------------------
# Assignment 2 - Conditions and comparison operators
# ----------------------
a = 10; b = 20;
# False
print(a, b, a == b, a > b, a>=b);
# True
print(a, b, a!= b, a < b, a <= b);


# ---------
# Conditional Branching
# ---------
a = 10; b = 20;


# if 
if a != b:
    print(a, b);


# if\else
if a == b:
    print(a, b);
else:
    print("a not equal b");
    input("Press enter to continue");
    
i = 100;
# if\elif\else
if i >= 80:
    print("Grade = A"); # i must be >= 80
elif i >= 60:
    print("Grade = C"); # i must be < 80 AND >= 60
elif i < 60:
    print("Grade = F"); # i must be < 60
else:
    print("In else and not possible");  # This should not happen
    
# ---------
# Code blocks
# ---------
count = 2;


if (count == 3):
    count += 10;
    print("Count = ", count);   # Count is not printed since count not equal 3


if (count == 3):
    count += 10;
print("Count = ", count);






#######################################################################################################################
## Lesson 03
# ----------------------
# Numeric data type, operators, variables
# ----------------------
print(10);      # Integer
print(3.1417);  # Float


# Printing operations on the "fly"
print(10+20);   # Addition
print(7/3);     # True division
print(7//3);    # Integer division
print(7%3);     # Remainder after Integer division


x = 5;      print(x);   # Defining  x as 5
x = x +2;   print(x);   # Increment x by 2 
x +=3;      print(x);   # Increment x by 3 
y = x +5;   print(y);   # Defining y as addition to x


# data type() function
type(y);        # Integer
y = 8.1;        # Explicit re- assigning y as 8.1 and type float.
type(y);        # Float


z = 6;      print(z, type(z));  # Assigning z as 6 and type int
z = z//2;   print(z, type(z));  # Explicit re-assigning z as 3 and type int 
z = z/2;    print(z, type(z));  # Implicit redefine z as 3.0 and type float


b = True;   print(b, type(b));  # Assigning b as a boolean True
b = 5 < 3;  print(b, type(b));  # Re-Assigning b as a boolean 




# ----------------------
# Type conversion, String Methods, String Functions
# ----------------------
## Type conversion
vi = input("Enter number ");        # User input a number as a string
print(vi, type(vi));
vi = vi +1;   # Error


vi = int(input("Enter number "));   # Data type conversion on input
print(vi, type(vi));


## String Function
s = 'the quick brown fox';
ls = len(s);
print(s, '\t', ls, '\t',type(ls));  # String length


## String Method
us = s.upper();
print(s, '\t', us, '\t',type(us));  # Upper case


# ----------------------
# String Methods and Functions
# ----------------------
s = 'the quick brown fox';


# String Methods
s.capitalize(); # Returns the string with first letter capitalized and the rest lowercased.
s.count('o');   # Count the non-overlapping occurrence of supplied substring in the string.
s.find('o');    # Return the index of the first occurrence of supplied substring in the string. Return -1 if not found.
s.lower();      # Return a copy of all lowercased string.
s.replace('o','a'); # Replace all old substrings with new substrings.
s.split(' ');   # Function returns a list of all the words in the string, using str as the separator 
s.strip('x');   # Return a string with provided leading and trailing characters removed.
s.swapcase();   # Return a string with lowercase characters converted to uppercase and vice versa.
s.title();      # Return a title (first character of each word capitalized, others lowercased) cased string.
s.upper();      # Return a copy of all uppercased string.


# String Function
len(s); # Function Returns the length of the string (i.e. number of characters).




#######################################################################################################################
## Lesson 02
# ----------------------
# Printing String Operations
# ----------------------
print('');              # Empty string
print('1a2B3c4D5');     # Alphanumeric
print('!@\#$%^&*()_');  # Symbol characters including '\'


print('Program "Game Over" 2.0');       # Quotes inside strings
print('Mixed', "quotes", '''here''');   # Mixed quotes here


print("Same Line "); print("New line");                 # Two commands with semi-colon ending
print("Same Line", end = " -> "); print("Same Line");   # Using end = 


print("First  " +  "Second  " + " Third");  # Concatenation
print("More " *3);                # Repeating
print("line 1 " \
     + " line 2");                # Line continuation


print("\nNewline before");        # New line escape sequences


print('Tab:\t', '-> to here', '\nthen next line');  # Tab and New line after escape sequences
print('!line 1\n line 2 \\n lines');    # Symbol characters with embedded special code


# ----------------------
# String Variables
# ----------------------
lname = '';         # Creating variable lname as string data type
lname = 'Smith';    # Defining lname as Smith
print(lname);            # Display contents of variable lname
lname = 'Jones';    # Re-Defining lname as Jones 
print(lname);            # Display contents of variable lname


fname = '';         # Creating variable fname as string data type
print(fname);            # Display contents of variable fname


fname = 'Jane';            # Defining fname as Jane
print(fname, " ", lname);    # Display full name


# ----------------------
# Python Program
# ----------------------
name = "Larry";     # Assign a string to variable 'name'
print(name);        # Print the variable content
print("Hi,", name); # Print a string and variable 
print("\n");        # New line


name = input("Hi.  What's your name? ");    # Get name from user
print("Hi,\t", name);   # Print name input from user after TAB


input("\n\nPress the enter key to exit.");  # Exit program






#######################################################################################################################
## Lesson 01
# ----------------------
# Interactive mode
# ----------------------
print('Letters: A sequence of characters'); 
print("Numbers: 0 1 2 3 4 5 6 7 8 9 ");
print("My name is: ");  # Type your name after the colon


print(Error);   # Error - no quote
print('Error"); # Error - mismatch quotes
print "Error";  # Error - No Parens






# ----------------------
# Script mode
# ----------------------
#   File -> New File
#   File -> Save As -> find your directory -> name your file
'''
Multi-Line documentation
print and input fuctions
'''
print('This is a string');
input("Press any key to see the next print");


print('Numbers: 0 1 2 3 4 5 6 7 8 9');
input("Press the Enter key to exit");


#######################################################################################################################