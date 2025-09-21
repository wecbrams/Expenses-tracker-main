file1 = open("f.txt", 'r')
file2 = open("f.txt", 'w')

for line in file1.readlines():
    if not (line.startswith("I am")):
        print(line)

        file2.write(line)

file2.close()
file1.close()