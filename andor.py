# number = int(input("Enter the number: "))

# o_number= number
# r_number = 0

# while number> 0:
#     digit =number % 10
#     r_number = r_number*10+digit
#     number//=10

# if o_number==r_number:
#     print(f"{o_number} is palindrome")
# else:
#      print(f"{o_number} is not a palindrome")





largestN= int(input("Enter the largest number: "))
smallestN= int(input("Enter the smallest number: "))

while(smallestN):
    nstore = smallestN
    smallestN= largestN % smallestN
    largestN = nstore
print("HCF/ GSF is: ",largestN)


