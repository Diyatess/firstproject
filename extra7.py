# Create a list
list = ["Apple", "Orange", "Banana", "Strawberry", "Mango"]

# Open a file to write
file = open("list.txt", "w")

# loop through the elements in the list
for element in list:
    # write each element to the file
    file.write(element + "\n")

# close the file
file.close()