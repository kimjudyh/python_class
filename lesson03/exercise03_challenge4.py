# lesson 03, chapt 2, challenge 4
'''
Write a Car Salesman program where the user enters the base price of a car.
The program should add on extra fees such as tax, license, dealer prep,
and destination charge. Make tax and license a percent of the base price.
The other fees should be set values.
Display the actual price of the car once all the extras are applied.'''

# variables
base = 0.0;                     # base price of car, float
total = 0.0;                    # total price of car
tax = .08;                      # 8% tax
licenseFee = .05;               # 5% license fee
dealerPrep = 100.00;            # dealer prep fee
destinationCharge = 150.00;     # destination charge fee

# user input
base = float(input("Enter the base price of the car: \n"));

# calcs
total = base + base*(tax + licenseFee) + dealerPrep + destinationCharge;

# display
print("The total price of the car is: $", end="");
print("{0:0.2f}".format(total));
