''' ######################################################################
Product list using nested dictionary of lists
Manage a Product list using nested dictionary of lists
    Module: import from Project_Data.py
    Load a dictionary from the list using the product number as key
         with value as a list of Description, Size and Sales Price.
    Menu items\options:
      - display the dictionary
      - delete product number
    Products List: l_prod
          Index 0 = Product number - String
          Index 1 = Product line   - String
          Index 2 = Size           - String
          Index 3 = Color          - String
          Index 4 = Price          - Float
    Function List
      - f_menu
      - f_list_to_dict
      - main
################################### '''
## Modules 
from Project_Data import l_prod;    # Import products list l_prod 


#################################################################
## Function definitions
#################################################################
def f_menu():
    ''' 
f_menu:
  Process: Display a menu of options for the user to choose from.
           Verify a valid choice is made and return it.
 Inputs: None
 Outputs: Menu option chosen
    '''
  # ---------------
  # Local variables
    option = '';
  
  # ---------------
  # Display Menu and get menu option
    print(
    """
    Products!
    1 - Load the Product dictionary
    2 - Display the Product dictionary
    x - Exit
    """
    )
    
    # ask user input
    option = input("Choose a menu option:\n")
    print()        
    return option;




#################################################################
def f_list_to_dict():
    ''' 
f_list_to_dic:
  Process: Loads a dictionary from the list using the first element as the key
           and the rest of the list as a value
  Inputs:  list
  Outputs: dictionary
    '''
    d_prod = {};     # Initialize Dictionary of product list
    
    for i in l_prod:    # loop through using list index
        d_prod[i[0]] = i[1:]    # make index 0 element the key, remainder into list

    # give some notification to user that it happened
    print("Dictionary loaded.\n")
    
    return d_prod;




#################################################################
def main():
 
 ## ------------------
 ## Initialize variables
    vs_choice = '';     # Menu choice
    d_prod    = {};     # Dictionary of product list


 ## ------------------
 ## Main Process 
    while vs_choice not in ['x','X']:
        vs_choice = f_menu();   # Display menu and get menu choice


     ## ------------------
     ## Conditional branching based on menu choice
     ## Exit
        if vs_choice.upper() == 'X': print("Good-bye.");


     ## ------------------
     ## Load the Product Dictionary
        elif vs_choice == '1':  
            print("Load Product Dictionary")
            d_prod = f_list_to_dict();
            input("Press enter to continue.\n")


     ## ------------------
     ## Display the Product Dictionary
        elif vs_choice == '2':
            print("Display Product Dictionary")
            
            if not d_prod:  # check that dictionary was initialized first!
                print("Need to load the product dictionary first.",
                    "Choose option 1.\n")
                input("Press enter to continue.\n")
                continue
            else:   # print key, value in rows
                for key, value in d_prod.items():
                    print(key, "\t", value, end="\n")
            
            
     ## ------------------
     ## Invalid menu choice
        else:
            print("Sorry, but", vs_choice, "isn't a valid choice.")
        
    input("\n\nPress the enter key to exit.")
    return;     # End of function main()


        
#################################################################
main();     # call main()
