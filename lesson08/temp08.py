# temp file for lesson 08

import operator as op
#from operator import itemgetter

list1 = [ [1, 6, 3],
          [3, 7, 0],
          [9, 4, 1]
        ]

ls = sorted(list1, key = op.itemgetter(1), reverse = False)
print(ls)
