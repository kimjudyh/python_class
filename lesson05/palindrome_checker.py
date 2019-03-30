# lesson 05
# palindrome checker

# variable
#ss = "Animal Loots Foliated Detail of Stool Lamina";
#ss = "Live dirt up a side track carted is a putrid evil";
#ss = "the brown fox jumped over the dog";
#ss = "racecar";
#ss = "Raw evil dam on Niagara Gain net time Sub bus emit ten Niagara Gain no mad live war";
#ss = "Able was I, ere I saw Elba.";
ss = "Campus motto: Bottoms up, Mac.";

length = len(ss);       # get length of string
p_index = 0;            # initialize positive index. [0:length-1]
n_index = -1;           # initialize negative index. [-1:-length]


# loop through string from beginning to end
# print each letter, ignoring spaces, on same line
while p_index < length:
    # ignore spaces
    if ss[p_index] == " ":                  # if it's a space
        p_index = p_index + 1;              # increase loop variable by 1
    else:
        print(ss[p_index].lower(), end=""); # print current char as lowercase
        p_index = p_index + 1;              # increase loop variable by 1

print();    # new line..

# loop through string from end to beginning
# print each letter, ignoreing spaces, on same line
while n_index >= -length:
    # ignore spaces
    if ss[n_index] == " ":
        n_index = n_index - 1;              # decrease loop var by 1
    else:
        print(ss[n_index].lower(), end=""); # print current char as lowercase
        n_index = n_index - 1;              # decrease loop var by 1

# visually check that both lines are same
print();    # new line

# Challenge 1
# loop through string from beginning to end
# compare each character from beg. to end with char from end to beg.
# display results as palindrome if character matches as it should

index = 0;                      # new index var
isPalindrome = True;            # set boolean to false for now
ss_new = ss.replace(" ","");    # remove spaces
length = len(ss_new);           # get length of no-space word
half = length//2;               # integer divide by 2, rounds down

if length%2 == 1:               # if num of chars is odd
    # don't need to compare middle char, evaluate while boolean is true
    while index < half and isPalindrome:  
        # if left side char equals right side char, in lowercase
        if ss_new[index].lower() == ss_new[(length-1)-index].lower():
            index = index + 1;      # increment index
        # if chars are not a match
        else:
            isPalindrome = False;   # set boolean to false, exit while loop
            
else:                           # if num of chars is even
    # last comparison is left and right around midpoint
    while index <= half and isPalindrome:    
        if ss_new[index].lower() == ss_new[(length-1)-index].lower():
            index = index + 1;
        else:
            isPalindrome = False;
            

# check what boolean was set to
if isPalindrome:
    print(ss, ": is a palindrome");
else:
    print("not a palindrome :(");
            

# Challenge 2
# loop through string from beginning to end
# compare each char from beg. to end w/ char from end to beg.
# use compound conditional expressions to check for punctuation
# display results as palindrom if character matches as it should

indexL = 0;
indexR = len(ss)-1;
print("length:", len(ss));
isPalindrome = True;

while indexL != indexR and isPalindrome:
    # check if left char is punctuation
    if ss[indexL] == "!" or ss[indexL] == "," or ss[indexL] == ":" \
       or ss[indexL] == "." or ss[indexL] == " ":
        print("puncL",indexL);
        indexL = indexL + 1;
        
    elif ss[indexR] == "!" or ss[indexR] == "," or ss[indexR] == ":" \
       or ss[indexR] == "." or ss[indexR] == " ":
        print("puncR",indexR);
        indexR = indexR - 1;

    elif ss[indexL].lower() == ss[indexR].lower():
        print("match");
        print(indexL, indexR);
        indexL += 1;
        indexR -= 1;
    else:
        print("not match", indexL, indexR);
        isPalindrome = False;

if isPalindrome:
    print("is a palindrome");
else:
    print("not a palindrome");
