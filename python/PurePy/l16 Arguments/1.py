def total_calc(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)

    print(f"Please pay ${total}")

total_calc(150,20)

'''
The following program is
about cuboid
'''
# function to find cube
def cube(num):
    return num * num * num

num = int(input("Please enter your number: "))
print(f"The cube of {num} is {cube(num)}")


 