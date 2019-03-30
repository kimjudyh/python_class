#######################################################################################################################
'''
Examples of Python Code Samples; examples.py
Contents:
  Lesson 01 - Print and Input commands
  Lesson 02 - Strings, variables
  Lesson 03 - Numeric data types, Operators, Type conversion, String methods
'''


#######################################################################################################################
## Lesson 03
# ----------------------
# Numeric data type, operators, variables
# ----------------------
print(10);      # Integer
print(3.1417);  # Float


# Printing operations on the "fly"
print(10+20);   # Addition
print(22/7);    # True division - Pi
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