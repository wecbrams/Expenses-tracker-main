# Program to append contents of one file to another
# Entering the file names
firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file: ")

# Opening both files in read-only mode to read initial contents
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

# Printing the contents of the files before appending
print('Content of first file before appending:\n', f1.read())
print('Content of second file before appending:\n', f2.read())

# Closing the files
f1.close()
f2.close()

# Opening first file in append+read mode and second file in read mode
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

# Appending the contents of the second file to the first file
f1.write(f2.read())

# Relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

# Printing the contents of the files after appending
print('Content of first file after appending:\n', f1.read())
print('Content of second file after appending:\n', f2.read())

# Closing the files
f1.close()
f2.close()
