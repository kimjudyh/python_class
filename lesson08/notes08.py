# lesson 08

'''
sequence sorting, itemgetter(), dictionaries
'''

# sequence sorting---
# sort method - in place, changes list. can't use on tuple. returns None.
# sorted() function - returns new list, original list not changed

list1 = [5, 1, 4, 3]
list1.sort()
print(list1)            # [1, 3, 4, 5]

list1 = [5, 1, 4, 3]
print(sorted(list1))    # [1, 3, 4, 5]
print(list1)            # [5, 1, 4, 3]

# sorted(sequence, key function, reverse)
# key function should function that takes single arg and returns a single value
list1 = ['ccc', 'aaa', 'd', 'bb']
print(sorted(list1, key = len, reverse = False))    # sort on string len
# output: ['d', 'bb', 'ccc', 'aaa']

# itemgetter()---
# sorting nested sequences
# need to import operator module
# operator.itemgetter(element): returns callable object that fetches element
#   from its operand

import operator
# or.. from operator import itemgetter
list1 = [[1, 5, 6],
         [1, 4, 6],
         [3, 3, 6]
        ]
ls = sorted(list1, key = operator.itemgetter(1), reverse = False)
# sort based on index 1 of each list (3,4,5)
print(ls)           # [[3, 3, 6], [1, 4, 6], [1, 5, 6]]

print(sorted(list1, key = operator.itemgetter(0, 1), reverse = True))
# sort first by index 0 then by index 1
# output: [[3, 3, 6], [1, 5, 6], [1, 4, 6]]

l_list = [ [1, 37, 3],
           [2, 4, 6],
           [3, 52, 7],
           [5, 8, 0]
        ]
for i in sorted(l_list, key = operator.itemgetter(1), reverse = False):
    print(i, i[0], i[1], i[2])
print(l_list)

# Say we have a list of strings we want to sort by the middle letter of the string.
strs = ['xdc', 'zab', 'ycd' ,'wba']

# Write a function that takes a string, and returns its 2nd to last letter.
# This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-2]

# Now pass key=MyFn to sorted() to sort by the middle letter:
print (sorted(strs, key=MyFn))  # ['zab', 'wba', 'ycd', 'xdc']

# dictionaries---
# each item is pair of key and value (mixed data types)
# indexed by keys (immutable), case sensitive, no duplicates
# values (mutable) don't have to be unique
# no concept of order or sequence among elements

d = {}                      # initialize dictionary
d = {'a':1, 'b':2, 'c':3}   # {key:value, key:value, key:value}
d1 = {1:'int', 2.2:'float', 'abc':'string'}

d['a']          # output: 1
type(d['a'])    # <class 'int'>

'a' in d;       # membership (key): True
'x' in d;       # False

# dictionary methods
d.get('a')      # returns value for given key: 1
d.keys()        # returns list of keys: dict_keys(['a', 'b', 'c'])
d.values()      # returns list of values: dict_values([1, 2, 3])
d.items()       # returns list of dictionary (key,value) tuple pairs
                # dict_items([('a', 1), ('b', 2), ('c', 3)])
d.copy()        # returns a deep copy

# dictionary functions
len(d)          # 3

# identify
d1 = d;         # shallow copy
d2 = d.copy()   # deep copy

# dictionary modification
d['x'] = 6      # add key:value pair of 'x':6
print(d)        # {'a': 1, 'b': 2, 'c': 3, 'x': 6}

d['x'] = 999    # update value for key 'x'
print(d)        # {'a': 1, 'b': 2, 'c': 3, 'x': 999}

del(d['c'])     # delete pair associated w/ key 'c'
print(d)        # {'a': 1, 'b': 2, 'x': 999}

# dictionary of lists
# allows for direct (vs sequential) access to list items associated w/ key
# can be used like an array, ie. row, column structure

d = { 'a':[1, 2, 3],
      'b':[2, 4, 6],
      'c':[3, 5, 7]
    }
print(d)            # {'a': [1, 2, 3], 'b': [2, 4, 6], 'c': [3, 5, 7]}

print(d['a'])       # access specific list using key: [1, 2, 3]
print(d['a'][2])    # access specific element in list: 3

# dictionary loops
# use items() method to get key and value at same time

d ={'a':1, 'b':2, 'c':3}

for key, value in d.items():
    print(key, value)

    # a 1
    # b 2
    # c 3

d = { 'a': (1, 2, 3),
      'b': (2, 4, 6),
      'c': (3, 5, 7)
    }

for key, value in d.items():
    print(key, value)

# Create a dictionary of lists from a list of lists 
l_list = [ [ 'a', 2, 'apple' ] 
          ,[ 'b', 4, 'bravo' ] 
          ,[ 'c', 5, 'crate' ] 
         ];     # list of lists - assume 1st element of each list is unique


d = {}; # Initialize an empty dictionary
for i in l_list:
    d[i[0]] = [int(i[1]), i[2]]; # Create the key i[0] and values list
print (d);      # {'a': [2, 'apple'], 'b': [4, 'bravo'], 'c': [5, 'crate']}




