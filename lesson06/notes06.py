# lesson 06

'''
for loops, range(), sequences, slices
'''

# for loops---
# for <identifier> in <sequence>:
#   <code block>
# can't change number of iterations by modifying identifier in loop!

for i in "Python":
    print(i, end=", ");

print();

for i in range(1,10,2):
    print(i, end=", ");

print();

# else clause - can tell you how you exited the loop
# if loop terminates from break, else block is skipped
# if loop terminates naturally, else block is executed

for num in range(0,5,1):
    if num == 22:
        print("\nexit loop");
        break;
    else: print(num, end="-");
else: print ("\n loop completed");

# membership operator
# in - is variable in sequence
# not in - is variable not in sequence

ss = "this is an example";
print("i" in ss);       # prints True
print("i" not in ss);   # prints False

punctuation = "?, .!:";  # string of punctuation characters
print ("In:  "   , '?' in     punctuation); # In:   True
print ("Not In: ", 'y' not in punctuation); # Not In:  True
print(punctuation in "Hi!");        # prints False
print("." in punctuation);          # prints True

# this code replaces any punctuation found in s with ""
s = "hello, my name is:";
punctuation = "?, .!:";  # string of punctuation characters
for i in punctuation:   # i becomes each char in punctuation string
    s = s.replace(i,"");    # replaces the punctuation repped by i with ""
print(s);

edibles = ["ham", "spam", "eggs", "nuts"];
for x in edibles:
    if x != "nuts":
        print("no nuts!!");
    else:
        print("finally, nuts");


# range() function---
# 1. range(start,stop,step) - recommend using this one for clarity
# 2. range(start,stop)
# 3. range(stop) - default start is 0
# stop - up to but not including this number

for i in range(5):
    print(i,end=", ");       # 0, 1, 2, 3, 4

for i in range(-5,0):
    print(i,end=", ");       # -5, -4, -3, -2, -1

for i in range(1,10,2):
   print(i, end=',');  # Odd numbers: 1,3,5,7,9,

print();
for i in range(5,0,-1):
   print(i, end=',');  # Backwards: 5,4,3,2,1,


# slicing sequences---
s = 'Python';
s[0:2];	        # = 'Py'
s[:3];       	# First 3 characters = 'Pyt' 
s[4:];	        # Remaining characters after the h = 'on'
s[:3]+s[4:];	# Original string with the 'h' removed = 'Pyton‘
s[:];           # All characters
s[0:0];         # End point = Start point = ''

print(s[0:6]);      # = 'Python'
print(s[0:len(s)]); # = 'Python'

print(s[0:2]);      # = 'Py'
print(s[:3]);       # First 3 characters = 'Pyt' 
print(s[4:]);       # Remaining characters after the h = 'on'
print(s[:3] + s[4:]);         # Original string with the ‘h’ removed 'Pyt' + 'on' = 'Pyton‘

# Special cases
print(s[:]);        # All characters
print(s[0:0]);      # End point = Start point = ''
print(s[3:1]);      # Illegal slice but no error = ''

print(s[::-1]);     # reverses the string

