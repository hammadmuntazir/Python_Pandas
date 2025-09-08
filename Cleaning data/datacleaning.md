#            Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates

  # Solution 1
#   -> removing row containing empty cells
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
# dropna() is used

# (2)          Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value: