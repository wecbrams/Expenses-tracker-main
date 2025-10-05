import turtle 
# Set up the screen
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")  # screen background color
my_wn.title("Turtle")

# Create the turtle
my_pen = turtle.Turtle()

# Set initial size
size = 0

# Infinite loop to draw expanding squares
while True:
    for i in range(4):
        my_pen.forward(size + 1)
        my_pen.left(90)
    size += 5  # Increase size for spiral effect
