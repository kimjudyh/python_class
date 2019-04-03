''' ######################################################################
Manage a word list using nested list of lists
    Module: import from module data list
    Menu items\options:
      - print list
      - add element
      - delete element
      - exit
    List structure:
      Index 0 = word
      Index 1 = length of word
      
######################################################################## ''' 
## Modules
from Lesson_07_Word_List import l_words;    # Word list


## Initialize Local variables
vs_choice = '';     # Menu choice
l_list = [];        # List of word, length to add
vs_word  = '';      # word to add
vi_item   = 0;      # List element index
replace_word = '';  # word to replace


# Loop on Menu options until finished
while vs_choice.upper() != 'X':
    print(
    """
    Manage a Word List
    
    1 - Display the list of words and the length
    2 - Add a word and its length
    3 - Replace a word
    x - Exit
    """
    )
    vs_choice = input("Choice: ")
    print()


  # Conditional Branching based on Menu choice
    # Exit
    if vs_choice.upper() == 'X':
        print("Good-bye.");


    elif vs_choice == '1':
        # print("Print the list of words AND length")
        
        for i in range(0, len(l_words), 1):
            print(str(i)+".", l_words[i][0]+ ", length:", l_words[i][1]);
        
    # Add a word
    elif vs_choice == '2':
        # print("Add a word");
        # todo
        # get input
        # get word length
        # put word and word length into a list
        # append list to existing l_words
        vs_word = input("Enter the new word: \n");
        l_list = [vs_word, len(vs_word)];
        l_words.append(l_list);

    # Replace a word
    elif vs_choice == '3':
        # type the index of the word you want to replace
        # type what you want to replace word with
        # get input
        # find word in list
        # replace word with new word
        # make sure input is valid!
        new_word = int(input("Type the index of the word you want to replace:\n"));
        vs_word = input("Type what you want to replace that word with:\n");        
        l_list = [vs_word, len(vs_word)];
        l_words[new_word] = l_list;
        
    # some unknown choice
    else:
        print("Sorry, but", vs_choice, "isn't a valid choice.")
  
input("\n\nPress the enter key to exit.")
