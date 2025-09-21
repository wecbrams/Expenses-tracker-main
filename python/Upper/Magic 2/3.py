a = 3000
for num in range(1, a + 1):
    c = 0
    temp = num
    for i in range(1, temp + 1):
        if temp % i == 0:
            c += 1
    if c == 2:  # It's a prime
        rev = 0
        t = num
        while t > 0:
            rev = rev * 10 + (t % 10)
            t \\= 10
        print("Palindrome numbers:\n")
        if rev == num:  # It's a palindrome too
            
            print(num)
            
            