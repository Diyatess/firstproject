
# Program to swap first and last element of a list

# Input List
list1 = [1, 2, 3, 4, 5]

# Storing first and last element as separate variables
first_ele = list1[0]
last_ele = list1[-1]

# Updating first and last element of the list
list1[0] = last_ele
list1[-1] = first_ele

# Printing the updated list
print(list1)