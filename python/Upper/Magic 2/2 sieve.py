def primeSeive(n):
    prime = [True for i in range(n + 1)]
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        if prime[currentNumber]:
            for i in range(currentNumber**2, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1
    prime[0] = prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            print(p)

n = int(input("Enter number to find all prime numbers less than the number: "))
primeSeive(n)
# 4 6 8 9 10 12 14 15 16 18 20 21 22 24 25 26 27 28 5
