def setornot(number,n):
    if number&(1<<(n-1)): #3  1<<3-1 == 1<<2
        print('\n Set')
    else:
        print('\nNot a Set')

number = int(input("Enter a number: "))
n = int(input("Enter a bit number: "))
setornot(number,n)