# lesson 11

'''
function scoping/global variables, passing parameters
'''

# function scoping---
# namespaces follow LEGB-hierarchy: Local, Enclosed, Global, Built-In
# scope directly related to level of block indentation

# local scope: x is defined in the function
def f1():
    x = 11
    print("inside f1: x = ", x)
    return
x = 1
f1()
print("outside f1: x = ",x)

# global scope: x is defined outside the function, so python goes global
def f1():
    print("inside f1: x = ", x)
    return
x = 2
f1()
print("outside f1: x = ",x)

# global keyword tells python to define var on global level
def f1():
    print("inside f1, x = ", x)
    print("inside f1, y = ", y)
    return
def main():
    global x    # global keyword
    x = 2
    f1()
    return
y = 5           # global var implicitly defined
main()

# built-in scope functions
# locals() - call inside a function
print("z" in locals())

# globals()
print("z" in globals())

def f1():
	print("In f1: 'z' in locals()?  ", 'z' in locals());    # False
	print("In f1: 'z' in globals()? ", 'z' in globals());   # False
	return;
def main():
	z = 9;	
	f1();
	print("In main: 'z' in locals()?  ", 'z' in locals());  # True
	print("In main: 'z' in globals()? ", 'z' in globals()); # False
	return;
main();

# enclosed example- function w/in function
def f1():
    def f1a():
        print("Inside f1a: x = ", x);	        # 2
        print("locals: ", x in locals());       # False
        print("globals: ", x in globals());     # False
        return;
    x = 2;
    f1a() 
    return; 

def main():
    f1();
    return;

main(); 

# modifying scope variables
# can read local variables, but can't modify
''' example
def f1():
	print(x);	# Can read contents of x
	x += 1;		# Trying to modify x -> ERROR
	return;
x = 1;		# x is in local scope
f1(); 
=> UnboundLocalError: local variable 'x' referenced before assignment
'''

# global declaration outside f1() and trying to modify inside f1()
'''
def f1():
	print(x);	# Can read contents of x
	x += 1;		# Trying to modify x -> ERROR
	return;
global x;	# x is declared global at Enclosed level
x = 1;	# x is assigned
f1();  
	=> UnboundLocalError: local variable 'x' referenced before assignment
'''

# global declaration inside function - not recommended
def f1():
	global x;	# x is declared global at Local level for modification
	print(x);	# Can read contents of x
	x += 1;		# Modifying x
	return;

x = 1;		# x in Global scope
f1();	
print("Outside f1: x = ", x); # Outside f1: x =  2

# passing parameters---
# pass by value - make copy in memory of actual value; immutable args
# pass by reference - copy of address of actual parameter is stored








