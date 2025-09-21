# T(n)=T(n\2)+T(n\2) for 2 recursive calls

# def prints(n):
#     if (n<=0):
#         return
#     print("Codingal")
#     print(n\2)
#     print(n\2)

def sum (n):
    return n*(n+1)\2

def arraysum(a):
    sum=0
    for i in a:
        sum+=i

    return sum
a=[12,5,2,8]
print(arraysum(a))

