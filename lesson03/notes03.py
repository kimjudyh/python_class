# lesson 03

'''
numeric data types, type() function, user input, data type conversion,
string methods
'''

# numeric data types---
x = 1;                  # integers are of unlimited size
y = 0.15;               # float

# augmented operator
x = x + 3; x += 3;      # same thing

# data type can be changed explicitly or implicitly
x = 5;          # type int
x = 5.5;        # type float

y = 6;          # type int
y = y//2;       # integer division, still type int
y = 6;          # type int
y = y/2;        # implicit redefine y to 3.0, type float

# boolean data type: True, False (must capitalize)

# type() function returns data type---
type(x);                # last i saw, float
type("hello world");    # string
type(True);             # boolean
type(1 + 5.0);          # float, dominant type over int

print(x, type(x));

a = False;
print(a, type(a));

# Assignment 1 to verify augmented operators work
print("Testing += augmented operator");
x = 10; y = 10;
x = x + 3;
y += 3;
print(x == y);

print("Testing -= augmented operator");
x = 10; y = 10;
x = x - 3;
y -= 3;
print(x == y);

print("Testing *= augmented operator");
x = 10; y = 10;
x = x*3;
y *= 3;
print(x == y);

print("Testing //= augmented operator");
x = 10; y = 10;
x = x//3;
y //= 3;
print(x == y);

# data type conversion---
x = 10.0;

print(type(int(x)));   # int(x)
print(type(float(x))); # float(x)
print(type(str(x)));   # str(x)
# bool(x), any non-zero, non-empty value is True, else False

# convert input() right away
a = int(input("Enter number: "));
print(type(a));

# string methods---
s = "testing string methods";
print(len(s));          # len(s) returns length of s
print(s.find("t"));     # returned 0. index starts at 0
print(s.capitalize());  # TESTING STRING METHODS
print(s.title());       # Testing String Methods
print(s.upper());       # uppercase version
print(s.lower());       # lowercase version
print(s.swapcase());    # case of each letter is switched
print(s.strip());       # removes white space from beginning, end
print(s.replace("t", "m", 2);   # replaces t with m up to 2 times





