import os

# create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

# check if file exists and delete it
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
else:
  print("The file does not exist")

# create file if it doesn't exist
with open("my_file.txt", "w") as my_file:
  my_file.write("Hi! I am Penguin and I am 1 yr old.")

# safely delete Codingal file
if os.path.exists('Codingal.txt'):
  os.remove('Codingal.txt')

# safely delete folder
if os.path.exists('Folder'):
  os.rmdir('Folder')