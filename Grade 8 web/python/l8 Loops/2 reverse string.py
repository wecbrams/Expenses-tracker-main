string = input("Enter your string: ")
string2 = ("")
for i in string:
    string2 = i+string2
print("\nThe Original String = ",string)
print("The reversed String = ",string2)

# Reverse order
n=int(input("Enter a value of n: "))
print("Numbers fom {0} to {1} are: ".format(n,1))

for i in range(n,0,-1):
    print(i)