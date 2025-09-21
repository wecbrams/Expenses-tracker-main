def numberOfBits(n):
    count = 0
    while n > 0:
        count += 1  
        n >>= 1
    return count
number=int(input("Enter your number: "))
print(f"Total bits: {numberOfBits(number)}")

# 101  