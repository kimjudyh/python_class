# lesson 10

'''
function parameters, formatting output, looping inside an outer loop
'''

# function parameters---
# ensure return vars are same data type as return value
# AND in the same order

def hello(n, msg):
    print(msg*n)
    return("complete", n+1)

status, n = hello(3, "mrow")    # output: mrowmrowmrow
print(status, n)                # output: complete 4

# parameter types - required, keyword, default, variable-length
# required arguments:
# # of args in function call must match exactly w/ function definition

# keyword arguments: caller identifies args by parameter name
# allows to skip arguments or place out of order
def printinfo(name, age):
    print("Name: ", name)
    print("Age: ", age)
    return

printinfo(age = 26, name = "hooty")

# default arguments: assumes default value if value not provided in call
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )
printinfo( name = "miki" )

# formatting output---
# template is string which contains 1 or more format codes (fields to be
# replaced) embedded in constant text
# fields to be replaced are surrounded by { }
'''
Example:  |{0:<8}|
| 	- Vertical bar displayed as a literal and field separator 
{}	- Curly braces define the contents to be displayed and the format
0	- Index to the item in the list of contents to be displayed
:	- Separator between the content index from the format specification
<	- Contents left justified the format (^ = centered,  > = right justified)
8	- Number of content characters to be displayed
'''

v_hdr_fmt = "|{0:^9}|{1:^6}|{2:^7}|{3:^7}|"	# header format
v_dat_fmt = "|{0:<9}|{1:>6}|{2:<7}|{3:<7}|"     # data format

print (v_hdr_fmt.format('-------', '-----', '----', '-----'));
print (v_hdr_fmt.format('Product', 'Price', 'Size', 'Color'));
print (v_hdr_fmt.format('-------', '-----', '-----', '-----'));
##for i in l_list: print (v_dat_fmt.format(i[0], i[1], i[2], i[3])); 

