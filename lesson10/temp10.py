# temp file for lesson 10

# Get products list
from Project_Data import l_prod;


# Set the report header and data format
#           Product,  Price, Size,   Color
v_hdr_fmt = "|{0:^15}|{1:^10}|{2:^7}|{3:^8}|{4:^8}|";  # Header format
v_dat_fmt = "|{0:^15}|{1:<10}|{2:>7}|{3:<8}|{4:<8}|";  # Data   format


# Display the report header
print (v_hdr_fmt.format('----------', '----------', '------', '--------', '--------'));   # Header data
print (v_hdr_fmt.format('Product', 'Product Num.'   , 'Price' , 'Size'    , 'Color'   ));   # Header data
print (v_hdr_fmt.format('----------', '----------', '------', '--------', '--------'));   # Header data


# Display the data
import operator;    ## Module for itemgetter
for i in sorted(l_prod, key=operator.itemgetter(1), reverse=True):
    print (v_dat_fmt.format(i[1], i[0], '${:,.2f}'.format(i[4]), i[2], i[3]));



