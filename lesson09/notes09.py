# lesson 09

'''
function basics, return values, documentation strings
'''

# function basics---
'''
def <function name> (<parameters>):
    <function body>
    return <results>
'''
# modular design decr complexity, encapsulation to protect internal data
def hooty_test(choice):
    new_choice = choice + 5
    return new_choice

def f_name():           # define function f_name, takes no inputs
    vi_var1 = 0         # local var
    print(vi_var1)
    return              # returns None; optional to put in but good practice

f_name()        # call function

# no params, no return values
def message():
    print("hello")
    return

message()

# no params, returns value
def menu():
    print("Menu")
    choice = 1
    return choice

v_option = menu()   # ensure returned var is same data type as returned value

# define an error status function
def f_err_mag():
    print("Application Error!")
    return

# call in main program
vb_err = True           # set error status
if vb_err: f_err_mag()  # call the function

# one return value function
def f_menu():
    choice = ""     # initialize variable
    while choice not in ("1", "2", "x", "X"):
        print('''
        Menu
        1. Option 1
        2. Option 2
        x. Exit
        ''')
        choice = input("Enter selection ")
    return choice.upper()       # return selection option

# call in main program
vs_opt = f_menu()       # get menu selection
print("Selection: ", vs_opt)

# return multiple values
def f_login():
    f_user = input("Enter username: ")
    f_pass = input("Enter password: ")
    f_acct = input("Enter account number: ")
    return f_user, f_pass, f_acct

# call in main
vs_user, vs_pass, vs_acct = f_login()
print("Username, password, account #: ", vs_user, vs_pass, vs_acct)

# with a parameter (attempt)

var1 = hooty_test(5)
print(var1)

# trying another parameter function
def hooty_square(my_num):
    squared = my_num*my_num
    return squared

squared = hooty_square(10)
print(squared)

# documentation strings and main()---
# provides way of associating documentation w/ functions
# create using triple quotes and indented as part of code block

def f_test():
    '''
Documentation: test the documentation string functionality
as long as triple quotes are indented, text doesn't need to be
    '''

print(f_test.__doc__)

# including a main function can provide logical structure
# but not required

def hello():
    print("hello")
    return

def main():
    print("this is main")
    hello()
    return

main()





