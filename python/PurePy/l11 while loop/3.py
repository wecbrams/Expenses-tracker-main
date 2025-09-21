num = int(input("Enter a number: "))

sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp \\= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


   """
   151  1^3 +5^3+1^3 = 151
   Armstrong number is a number that is equal to the sum of 
   its own digits each raised to the power of the number of digits.

   153 1^3 + 5^3 + 3^3
   """