print("Merging two files...")

with open('Codingal.txt', 'r') as file1, open('sample_doc.txt', 'r') as file2:
    data1 = file1.read()
    data2 = file2.read()

merged_data = data1 + "\n" + data2

with open('MergedFile.txt', 'w') as output:
    output.write(merged_data)