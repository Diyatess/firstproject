#Write a Python program to check if a file is closed or not.

# Sample file
f = open("deoo.txt", "r")

# Check if file is closed
if f.closed == True:
  print("File is closed")
else:
  print("File is open")

# Close file
f.close()

# Check if file is closed
if f.closed == True:
  print("File is closed")
else:
  print("File is open")