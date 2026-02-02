def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"Please pay ${total}")

total_calc(150,20)


# Cube of the cube
def cube(num):
    return num*num*num
def by_three(num):
    if num %3==0:
        return cube(num)
    else:
        return False

print(by_three(9))
print(by_three(4))