import turtle    # importing library

screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(300, 400)

polygon = turtle.Turtle()  # Turtle object

num_sides = 6
side_length = 70
angle = 360 / num_sides

# Draw the polygon
for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
