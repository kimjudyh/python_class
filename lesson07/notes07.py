# lesson 07

'''
mutability, tuples, lists, nested sequences
'''

# mutability---
# mutable - can be modified "in place"
#   - list, dict
# immutable - can't be changed but return new objects when attempting
#   to modify.
#   - int, float, bool, string, tuple

ss = "string";      # variable assignment
ss = "newstring";   # variable reassignment

# this will give error:
# ss[0] = "x";

# tuples---
# type of sequence like strings but can contain multiple elements of
#   mixed data types

t1 = (1, 2, 3, 4, 5);           # tuple of integers
t2 = ('a', 1, 2.0, False);      # tuple of mixed data types
t3 = (1,);                      # One element tuple MUST have a comma
t4 = ();                        # Empty tuple
print(t1); print(t2); print(t3); print(t4);

len(t2);                # length of tuple: 4
"b" in t2;              # membership: False
for i in t2:            # iteration: a, 1, 2.0, False,
    print(i,end=", ");  # i takes on value AND data type
t1 + t2;                # concatenation: (1, 2, 3, 4, 5, 'a', 1, 2.0, False)
print("Slice of element 1 and 2: ", t1[1:3]);    # Slice 
print();

print(max(t1));         # returns item w/ max value
print(min(t1));         # returns item w/ min value

# list---
# can be modified, can be of mixed data types, can be sorted in place
# can't create new element
l_list = [1, 2, 3, 4, 5, 6];
print(len(l_list));     # length of list: 6
print(l_list[1:3]);     # slice: [2, 3]
print(3 in l_list);     # membership: True
l_list2 = [1, 2, 3];    
print(l_list+l_list2);  # concatenation: [1, 2, 3, 4, 5, 6, 1, 2, 3]

# can delete elements using an index
l_list = [1, 2, 3, 4, 5, 6];
del l_list[1];          # delete 2nd item/index#1 item
print(l_list);          # [1, 3, 4, 5, 6]

l_list = ['a', 'b', 'c', 'd', 'e', 'f'];
del l_list[1:3];	# delete a slice
print(l_list);          # ['a', 'd', 'e', 'f']

# list methods: remove, append, copy
l_list = [1, 2, 3, 4, 5, 4];
l_list.remove(4);       # remove the 1st occurence of VALUE 4, not index#4
print(l_list);          # [1, 2, 3, 5, 4]

l_list = [1,2,3,4,5,6];
l_list2 = ['a', 'b', 'c'];
l_list.append(l_list2);     # append list2 to list
print(l_list);              # [1,2,3,4,5,6,'a', 'b', 'c']

l_list = [1,2,3,4,5,6];
ss = 'x,y,z';               # make string
l_list.append(ss);          # append to list
print(l_list);              # [1, 2, 3, 4, 5, 6, 'x, y, z'] ss is one element

# shallow copy: when = operator is used
# both variables simply point to the same list
# if one variable is changed, the other is changed too
l_list = [1,2,3,4,5,6];
l_list2 = l_list;       # shallow copy
l_list[0] = 11;         # change 1st index in one var
print(l_list, l_list2); # both are now changed

# deep copy: returns new list, not just a pointer to original list
l_list = [1,2,3,4];
l_list2 = l_list.copy();    # deep copy
l_list[0] = 11;         # change 1st index in one var
print(l_list, l_list2); # only l_list is changed

# nested sequences---
# list of lists, list, dictionary of lists
l_list = [[1, 2, 3],
          [2, 3, 4],
          [3, 4, 5]];
print(l_list);          #m[[1, 2, 3], [2, 3, 4], [3, 4, 5]]

print(l_list[0]);       # access list in index#0: [1, 2, 3]
print(l_list[0][2]);    # access index#2 (3rd) in index#0 (1st) list: 3

list2 = ['x', 'y', 'z'];
l_list.append(list2);   # append a list
print(l_list);          # [[1, 2, 3], [2, 4, 6], [3, 5, 7], ['x', 'y', 'z']]
        
# looping through a list of lists using range()
for i in range(0, len(l_list), 1):    # Display the index associated with each element in the list
    print(i, ": ", l_list[i]);
i = int(input("Enter the index of an element to delete: "));   # User choose the index of the list
del l_list[i];  # Remove the list at the index position
print("\nNew list of lists: ", l_list);








