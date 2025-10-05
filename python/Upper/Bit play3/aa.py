def swap(a,b):
    a=a^b # 101 ^ 011 =    110
    b=a^b # 110 ^ 011 =  101    
    a=a^b # 110 ^ 101 = 011
    print(f"After swapping: \na = {a}\nb = {b}")

def swap2(a,b):
    a = (a &b)+(a|b)  # & 1 | 7 =8
    b= a+ (~b)+1  # 8 +(-4)+1 = 5
    a= a+ (~b)+1  # 8 + (-6) +1 =3
    print(f"After swapping: \na = {a}\nb = {b}")


