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
from Project_Data import l_prod    # Import products list l_prod
from Project_Data import l_ord     # Import order list l_ord
    

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
    option = ''
  
  # ---------------
  # Display Menu and get menu option
    print(
    """
    Products!
    1 - Load the Product dictionary
    2 - Display the Product dictionary
    3 - Combine the Product Orders
    4 - Display the combined Product/Orders
    x - Exit
    """
    )
    
    # ask user input
    option = input("Choose a menu option:\n")
    print()        
    return option




#################################################################
def f_list_to_dict():
    ''' 
f_list_to_dic:
  Process: Loads a dictionary from the list using the first element as the key
           and the rest of the list as a value
  Inputs:  list
  Outputs: dictionary
    '''
    d_prod = {}     # Initialize Dictionary of product list
    
    for i in l_prod:    # loop through using list index
        d_prod[i[0]] = i[1:]    # make index 0 element the key, remainder into list

    # give some notification to user that it happened
    print("Dictionary loaded.\n")
    
    return d_prod

################################################################
def f_combine(d_prod, l_ord):
    '''
Process:  Create a new list containing the each product and attributes and total order
quantity for the product
input parameters: product dictionary 
 l_ord	- list of orders
return value: combined product order list:
Index 0 = Product number		- String
Index 1 = Product line   		- String
Index 2 = Size           		- String
Index 3 = Color 		        - String
Index 4 = Price          		- Float
Index 5 = Total Order quantity 	- Integer
'''
    # todo
    # initialize list that contains combined data
    l_combine = []

    # for each key in d_prod
    for key, value in d_prod.items():
        
        # initialize total qty as 0
        total_qty = 0
        
        # for length of l_ord
        for i in l_ord:
            
            # if key == product number
            if key == i[1]:
                # add to total qty
                total_qty += i[2]

        # make new list entry for current product number
        l_combine.append([key] + value + [total_qty])


    return l_combine
    
################################################################
def f_display_combine(l_combine):
    '''
Process:  Display the contents of the product order structure with the
total order quantities, passed in as a parameter.
 input parameters: list of product orders to display
return value: None
'''
    # import module for itemgetter
    import operator
    
    # set report header and data format
    hdr_fmt = "|{0:^12}|{1:^16}|{2:^7}|{3:^8}|{4:^8}|{5:^10}|"  # Header format
    dat_fmt = "|{0:^12}|{1:<16}|{2:>7}|{3:^8}|{4:<8}|{5:^10}|"  # Data   format

    # Display the report header
    print (hdr_fmt.format('------------', '--------------', '------',\
                          '--------', '--------', '--------'))
    print (hdr_fmt.format('1', '2', '3', '4', '5', '6'))
    print (hdr_fmt.format('Product Num.', 'Product Line', 'Size', 'Color',\
                            'Price', 'Total Qty'   ))   
    print (hdr_fmt.format('------------', '--------------', '------',\
                          '--------', '--------', '--------'))   

    # ask how to person wants to sort by:
    num_sort = int(input("How would you like to sort the report? Enter a column number:\n"))

    # Display the report header
    print (hdr_fmt.format('------------', '--------------', '------',\
                          '--------', '--------', '--------'))
    print (hdr_fmt.format('1', '2', '3', '4', '5', '6'))
    print (hdr_fmt.format('Product Num.', 'Product Line', 'Size', 'Color',\
                            'Price', 'Total Qty'   ))
    print (hdr_fmt.format('------------', '--------------', '------',\
                          '--------', '--------', '--------'))

    # display the formatted data in l_combine
    # sort on num_sort minus 1 to account for person starting column count from 1
    for i in sorted(l_combine, key = operator.itemgetter(num_sort-1), reverse = True):
        print(dat_fmt.format(i[0], i[1], i[2], i[3], '${:,.2f}'.format(i[4]),
                             i[5]))

    return

#################################################################
def main():
 
 ## ------------------
 ## Initialize variables
    vs_choice = ''     # Menu choice
    d_prod    = {}     # Dictionary of product list
    l_combine = []      # list of combined order data list


 ## ------------------
 ## Main Process 
    while vs_choice not in ['x','X']:
        vs_choice = f_menu()   # Display menu and get menu choice


     ## ------------------
     ## Conditional branching based on menu choice
     ## Exit
        if vs_choice.upper() == 'X': print("Good-bye.")


     ## ------------------
     ## Load the Product Dictionary
        elif vs_choice == '1':  
            print("Load Product Dictionary")
            d_prod = f_list_to_dict()
##            input("Press enter to continue.\n")


     ## ------------------
     ## Display the Product Dictionary
        elif vs_choice == '2':
            print("Display Product Dictionary")
            
            if not d_prod:  # check that dictionary was initialized first!
                print("Need to load the product dictionary first.",
                    "Choose option 1.\n")
##                input("Press enter to continue.\n")
                continue
            else:   # print key, value in rows
                for key, value in d_prod.items():
                    print(key, "\t", value, end="\n")

     ## --------------------
     ##  Combine Product Orders
        elif vs_choice == '3':
            l_combine = f_combine(d_prod, l_ord)
            print("Products and Orders combined.")

     ## --------------------
     ## Display combined Product\Orders
        elif vs_choice == '4':
            # check that combined list was made
            if not l_combine:
                print("Need to combine order and product info first.",
                      "Choose option 3.\n")
                continue
            else:
                f_display_combine(l_combine)

            
     ## ------------------
     ## Invalid menu choice
        else:
            print("Sorry, but", vs_choice, "isn't a valid choice.")
        
##    input("\n\nPress the enter key to exit.")
    return     # End of function main()


        
#################################################################
main()     # call main()
