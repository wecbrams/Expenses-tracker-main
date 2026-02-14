import turtle


sc=turtle.Screen()
sc.bgcolor("lightblue")
sc.setup(500,350)

turtle.title("Welcome to the world of turtle")
board=turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1

turtle.done()