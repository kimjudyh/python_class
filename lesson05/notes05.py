# lesson 05

'''
while loops, logical operators, indexing
'''

# while loops---
# while condition is true:
#   conditional statements;
count = 10;                 # initialize loop variable
while count > 0:            # check loop variable
    print(count);
    count = count - 1;      # update loop variable
print("\nend of count");

# break; terminates current loop, resumes execution after loop block
# continue; returns to beginning of while loop
# pass; used bc a statement is required for syntax, but don't want to
#   execute any code. Is a null operation.

# ----------------------
# Option Menu with while loop and conditional branching
# There is a logic error in the conditional branching for 'x'
# How should it be fixed?
# ----------------------
# answer: doesn't take into account capitalized 'x'
# fix: make input lower case

vs_choice = '';                 # Initialize the option choice loop variable
while vs_choice != 'x': # Check loop variable
    print("\nChoose a color for your new car"); 
    print(" 1. Red    ");
    print(" 2. Green  ");
    print(" 3. Yellow ");
    print(" 4. Blue   ");
    print(" x. Exit   ");

  # Get menu choice - Update loop variable
    #vs_choice = input("\nEnter the number for your choice of color: "); 
    vs_choice = input("\nEnter the number for your choice of color: ").lower(); 
    # interestingly, only works to put .lower() here bc while, elif conditions
    # looking for lower case 'x'.
    
    if   vs_choice == '1':
       print("You chose Red    ");    
    elif vs_choice == '2':
       print("You chose Green  ");
    elif vs_choice == '3':
       print("You chose Yellow ");
    elif vs_choice == '4':
       print("You chose Blue   ");
    elif vs_choice == 'x':
       print("You chose Exit   ");
    else:
       print("\nThat is not a valid choice");
# End of while loop
print("exit");

# logical operators---
# and, or, not
score = 78;
if score < 80 and score > 70:
    print(score);
if not(score>80):
    print(score);

# indexing---
# positive and negative indexing
# positive index starts at 0
# negative index (right to left) starts at -1
ss = "Sammy shark!";
print(ss[0]);           # output: S
print(ss[-12]);         # output: S
print(ss[-1]);          # output: !
print(ss[11]);          # output: !
print(len(ss));         # output: 12
print(ss[6:11]);        # output: shark
print(ss[:5]);          # output: Sammy
print(ss[7:]);          # output: hark!


