# lesson 02

'''
strings, string variables
'''

# strings ---

print("comma", "gives", "space");               # comma
# comma gives space
print("hello", end=""); print("same line");     # end=
# hellosame line
print("concatenate"+"With"+"Plus"+"Sign");      # +
# concatenateWithPlusSign
print("repeat " *3);                            # *
# repeat repeat repeat 
print("line continuation", \
    "with backslash");                          # slash
# line continuation with backslash
print("new \nline")                             # \n
# new 
# line
print("testing out ", end="blahdida ");
print("same line end=");
# testing out blahdida same line end=
print("hello" + "\nlala");
# hello
# lala
print("hello \nlala");
# hello 
# lala
print("hello \tlala");
# hello 	lala

print("testing \\ slash \n lala\\n testing");
''' output
testing \ slash 
 lala\n testing
'''
print("test \\n stuff");
''' output
test \n stuff
'''
print("hello \\\ triple slash \\\n what happens");
''' ouput
hello \\ triple slash \
 what happens
'''

# string variables ---

myName = "";
print(myName);
myName = "Judy";
print(myName);
myName = "Judy" + "Kim";
print(myName);
fname = "judy";
lname = "kim";
print(fname, lname);

# input function ---
name = input("what's your name?\n");
print("Hi,\t", name);
