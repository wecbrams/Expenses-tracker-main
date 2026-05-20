file=open("Codingal.txt","r")
print(file.read())
file.close()

file=open("Codingal.txt","r")
print("Printing only parts of a file\n")
print(file.read(8))
file.close()

file=open("Codingal.txt","a")
file.write("Hi, todau is an mazing day to work with files")
file.close()