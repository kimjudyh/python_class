# lesson 04

'''
importing modules, conditions, conditional branching, code blocks
'''

# python modules---
# module is a file w/ python code, can define functions, classes, vars
# import statement: import modulename;
# from...import statement: from modulename import name1
# usage syntax: modulename.methodname(params)
# list of available modules: help("modules");

'''
from os import system;

system("python -m pip install --upgrade pip");  # install latest pip 
system("pip install openpyxl");	   # install excel module
	
system("pip uninstall openpyxl"); # Un-install excel module
'''

import random;
rand_nbr = random.randint(1, 6); print(rand_nbr); # randint 1-6 inclusive
rand_nbr = random.randrange(6);  print(rand_nbr); # randrange 0-5

from random import randint, randrange;
rand_nbr = randint(1, 6); print(rand_nbr); # randint 1-6 inclusive
rand_nbr = randrange(6);  print(rand_nbr); # randrange 0-5

# conditions, branching---
# non-zero AND non-null -> True
# zero OR null -> False
''' syntax:
if condition:
    code
---------------
if condition:
    code
else:
    code
---------------
if condition:
    code
elif condition:
    code
elif condition:
    code
else:           recommend using else as error check
    code
'''

a = 1; b = 2;

if a != b:
    print(a, b);

if a == b:
    print(a, b);
else:
    print("a does not equal b");

i = 60;
if i >= 80:
    print(i, "first option");
elif i >=60:
    print(i, "second option");
elif i < 60:
    print(i, "third option");
else:
    print(i, "not possible");

# code blocks---
# one or more consecutive lines indented by same amount
count = 2;


if (count == 3):
    count += 10;
    print("Count = ", count);   # Count is not printed since count not equal 3

# different result if print outside of indentation 
if (count == 3):
    count += 10;
print("Count = ", count);












