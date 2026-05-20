print("Eliminating duplicate lines...")

lines_seen = set()

with open('Repeated.txt', 'r') as inputFile, open('UpdatedFile.txt', 'w') as outputFile: 
    for line in inputFile:
        if line not in lines_seen:
            outputFile.write(line)
            lines_seen.add(line)