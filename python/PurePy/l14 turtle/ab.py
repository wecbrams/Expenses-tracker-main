import turtle

sc = turtle.Screen()

sc.bgcolor("darkblue")

sc.setup(500,350)

turtle.title("---> Welcome to world of turtle <---")

board=turtle.Turtle()

for i in range(4):

    board.forward(100)

    board.left(90)

    i=i+1