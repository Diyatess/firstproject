
# open the source file in read mode
with open('alphabets.txt', 'r') as source_file:
    # open the target file in write mode
    with open('target_file.txt', 'w') as target_file:
        # read the source file line by line
        for line in source_file:
            # write the line in target file
            target_file.write(line)

# print success message
print('File copied successfully!')