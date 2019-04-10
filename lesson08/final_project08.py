# final project

# uses file Project_Data.py, which contains a list of products and info:
#   product number: string
#   product line:   string
#   size:           string
#   color:          string
#   price:          float


# Import the l_prod list of lists from the data file Project_Data.py
# (i.e. from Project_Data import l_prod).

from Project_Data import l_prod


# Load a dictionary from the l_prod list of lists using the Product Number
# as the key and the product number attributes (Product Line, Size, Color,
# Sales Price) as the values in a list –> giving a dictionary of lists. 

# initialize dictionary
d_prod = {}


# Display a menu with the following options:
# 1. Load the Product dictionary.  Initialize an empty dictionary and load it
# from imported l_prod
# 2. Display the Product dictionary.  Print the key and the values list.
# 3. Exit the program if ‘x’ is entered.

# Initialize local variables
# input from user
u_choice = ''


# create while loop where runs while input != 'x'
while u_choice.lower() != 'x':
    # display choices menu
    print(
    """
    Products!
    1 - Load the Product dictionary
    2 - Display the Product dictionary
    x - Exit
    """
    )
    
    # ask user input
    u_choice = input("Choose a menu option:\n")
    print()
    
    # if choice is 'x', exit
    if u_choice.lower() == 'x':
        print("Goodbye.\n")
        
    # if choice is 1, load product dictionary
    elif u_choice == '1':

        # loop through using list index
        #   make index 0 element the key
        #   make remaining list the value
        for i in l_prod:
            d_prod[i[0]] = i[1:]

        # give some notification to user that it happened
        print("Dictionary loaded.\n")
        
    # if choice is 2, display product dictionary
    elif u_choice == '2':
        # check that dictionary was initialized first!
        if not d_prod:
            print("Need to load the product dictionary first.",
                    "Choose option 1.\n")
            continue
        else:
            for key, value in d_prod.items():
                print(key, "\t", value, end="\n")
            
    # some unknown choice
    else:
        print("Not a valid choice")

input("\nPress the enter key to exit.")




