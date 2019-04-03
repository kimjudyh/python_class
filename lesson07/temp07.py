# temp07

l_list = [ [ 1, 2, 3 ] 
          ,[ 2, 4, 6 ] 
          ,[ 3, 5, 7 ] 
         ];
i = int(input("Enter the first number of a list to add: "));
add_list = [ i, i*10, i-10 ];   # Add a list with [the entered number, number times 10, number - 10]
l_list.append(add_list);
print(l_list);
