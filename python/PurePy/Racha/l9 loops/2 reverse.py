string=input("Enter a string: ")

r_string=""
for char in string:
    r_string=char+r_string
print(f"The reverse of {string} is {r_string}\n")

num=int(input("Enter a value: "))
print("Numbers from {0} to {1} are".format(num,1))
for i in range(num,0,-1):
    print(i)