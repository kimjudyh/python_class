# lesson 04
# Secret Number Math Trick: guess the number a friend inputs based on
# their result from a sequence of operations.

# variables
secretNum = 0;      # friend's input [1,20]
faveMonth = 0;      # friend's input [1,12]
faveDay = 0;        # friend's input [1,31]
result = 0;         # friend's result after their calcs
guess = 0;          # mathemagician's guess

# input: ask for secret number
secretNum = int(input("Enter a secret number between 1 and 20"\
                      " (no decimal places!): \n"));
# check that it is between the limits
while (secretNum < 1 or secretNum > 20):
    secretNum = int(input("Enter a valid number between 1 and 20!:\n"));

faveMonth = int(input("Enter the number of your favorite month (1-12): \n"));
# check limits
while (faveMonth < 1 or faveMonth > 12):
    faveMonth = int(input("Enter a valid month between 1 and 12!:\n"));
    
faveDay = int(input("Enter the number of your favorite day (1-31): \n"));
# check limits
while (faveDay < 1 or faveDay > 31):
    faveDay = int(input("Enter a valid number between 1 and 31!:\n"));

# friend's part: calculating stuff w/ their secret number
result = secretNum*3;           # multiply by 3
result += secretNum;            # add the secret number
result -= 5;                    # subtract 5
result *= 3;                    # multiply by 3
result *= 3;                    # multiply by 3 again
result += secretNum;            # add secret number
result -= faveMonth;            # subtract favorite month
result *= 27;                   # multiply by 3 3x (27)
result += secretNum;            # add secret number
result -= faveDay;              # subtract favorite day
print("Here's my result:", result);
input("Press enter to see your secret number!");

# mathemagician's part
# if result is negative, secret number is 1
if result < 0:
    guess = 1;
    print("Your secret number is 1");
# if result has 3 digits, secret number is 2
elif len(str(result)) == 3:
    guess = 2;
    print("Your secret number is 2");
# else, ignore last 3 digits, add 2
elif result >= 1000:
    guess = (result//1000) + 2;
    print("Your secret number is", guess);
else:
    print("You broke the rules!");
    
