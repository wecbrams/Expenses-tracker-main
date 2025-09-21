import turtle

turtle.Screen().bgcolor("lightblue")
sc=turtle.Screen()
sc.setup(500,350)

turtle.title("Welcome to the world of turtle")
board=turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1