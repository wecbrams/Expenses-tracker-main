# from random import randint
# def get_number():
#     while True:
#         Num = int(input("Please enter a number between 1-10:"))
#         if 1<=Num<=10:
#             return Num
#         else:
#             print('Number invalid, try again')

# Num = get_number()
# print("You chose", Num,"!")

# Rando = randint(1,10)

# if Num == Rando:
#     print("You got the number!!")
# else:
#     print("Try again the number was", Rando)

from random import randint

def get_number():
    while True:
        try:
            num = int(input("Please enter a number between 1-10: "))
            if 1 <= num <= 10:
                return num
            else:
                print("Number invalid, try again.")
        except ValueError:
            print("Please enter a valid integer.")

rando = randint(1, 10)
while True:
    num = get_number()
    if num == rando:
        print("You got the number!!")
        break
    elif num < rando:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
