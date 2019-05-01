# lesson 12

'''
handling exceptions, csv
'''

import csv
lst = []

# using DictReader
# can access column by column header
# use newline='' to omit \n
try:
    file = open('products_csv.csv', newline='')
    reader = csv.DictReader(file)
except Exception as e:
    print("File processing error: " + str(e))

for i_row in reader:
    temp = [i_row['prod_nbr'], float(i_row['price']),
            i_row['size'], i_row['color'], i_row['prod_line']]
    lst.append(temp)

file.close()

for i in lst:
    print(i)

# using reader
# loads each row as list
# need to access with index, includes the first row which might be headers
lst = []
r_cnt = 0

try:
    file = open('orders_csv.csv', newline='')
    reader = csv.reader(file)
except Exception as e:
    print("file processing error: " + str(e))

for l_row in reader:
    # skip first line
    if r_cnt == 0:
        r_cnt += 1
        continue
    lst.append(l_row)

file.close()
for i in lst:
    print(i)



    
