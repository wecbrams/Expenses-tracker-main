# Program to remove lines starting with any prefix

file1 = open('Codingal.txt', 'r')
file2 = open('CodingalUpdated.txt', 'w')

for line in file1:   
    if not line.startswith('Coding'):
        print(line, end='') 
        
        file2.write(line)

# close and save the files
file1.close()
file2.close()