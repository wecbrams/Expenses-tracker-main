# Open the file in read mode
file_read = open('C:\Users\we4Trust\Downloads\Expenses-tracker-main\python\Upper\l9 File handling\Codingal.txt', 'r')
print("File in Read Mode-")
print(file_read.read())
file_read.close()

# Open the file in write mode
file_write = open('Codingal.txt', 'w')
# Write in the file
file_write.write("File in write mode....\n")
file_write.write("Hi! I am Penguin. I am 1 yr. old\n")
file_write.close()

# Open the file in append mode
file_append = open('Codingal.txt', 'a')
# Append in the file
file_append.write("File in append mode ....\n")
file_append.write("Hi! I am Penguin. I am 1 yr. old\n")
file_append.close()
