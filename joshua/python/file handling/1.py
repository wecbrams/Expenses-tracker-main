# VISUAL STUDIO CODE

# open file and store file object in a variable
file = open('Codingal.txt')
# read the contents of file
print(file.read())
# close the file
file.close()

# open the file in read mode
file_read = open('Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal.txt', 'w')
# write in the file 
file_write.write("File in write mode ....\n")
file_write.write("Hi! I am Penguin. I am 1 yr. old\n")
file_write.close()

# open the file in append mode
file_append = open('Codingal.txt', 'a')
# append in the file 
file_append.write("\nFile in append mode ....\n")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()

# open file again to read updated content
file = open("Codingal.txt","r")
# read content
Content = file.read()
print("\nUpdated File Content:\n")
print(Content)
# count number of lines
Counter = 0
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1
print("\nThis is the number of lines in the file:")
print(Counter)

file.close()