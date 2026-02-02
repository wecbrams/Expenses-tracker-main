a = input("Enter a word: ")
for i in a:
    if(i=="A"):
        print("A is found")
        break
    else:
        print("A not found")

for i in range(10):
    if i%20==0:
        print("Twist")
    elif i%15==0:
        pass
    elif i % 5:
        print("fizz")
    elif i % 3:
        print("buzz")
    else:
        print(i)

# COntinue 
var =10
while var >0:
    if var == 5:
        var -=1
        continue
    print("Current variable value : ",var)
    var -=1
print("Good bye")


def find_first_set_bit(n):
    if n==0:
        return -1
    position =0
    while (n&1) ==0:
        n >>=1
        position +=1
    return position
number =8
first_set_bit_position =find_first_set_bit(number)
print(f"The first set position : {first_set_bit_position}")