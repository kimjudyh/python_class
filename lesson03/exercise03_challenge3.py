# lesson 03, chapt 2, challenge 3
'''
Write a Tipper program where the user enters a restaurant bill total.
The program should then display two amounts: a 15 percent tip and a
20 percent tip.
'''

# initialize variables
bill = 0.0;     # float
tip15 = 0.0;
tip20 = 0.0;

# user input
bill = float(input("Enter the bill amount: "));

# calculations
tip15 = bill*.15;   # calcs 15% tip
tip20 = bill*.2;    # calcs 20% tip

# display results
print("15% Tip Amount: $" + "{0:0.2f}".format(tip15));
print("20% Tip Amount: $" + "{:.2f}".format(tip20));
