import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("Aqua")

# Create the turtle
board = turtle.Turtle()

# First triangle for star
board.forward(100)     # Draw base
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

# Move to position for second triangle
board.penup()
board.right(150)
board.forward(50)
board.pendown()

# Second triangle for star
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

# Finish
turtle.done()
