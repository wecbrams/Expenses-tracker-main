# Initial values
a = 18
b = 12
c = 8
# Check if all variables have a boolean value of True (i.e., are non-zero)
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("At least one number has boolean value as False")
# New values for next test
a = 10
b = -5
c = 8
# Check if either 'a' or 'b' is greater than 0
if a > 0 or b > 0:
    print("Either of the numbers is greater than 0")
else:
    print("No number is greater than 0")
# Check if 'b' or 'c' is greater than 8
if b > 8 or c > 8:
    print("Either of the numbers is greater than 8")
else:
    print("No number is greater than 8")
