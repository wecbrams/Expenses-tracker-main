# import turtle

# # Setup the screen
# sc = turtle.Screen()
# sc.bgcolor('lightblue')
# sc.setup(500, 600)

# # Create a turtle
# t = turtle.Turtle()

# # Function to draw a triangle
# def draw_triangle(size=200, color="blue"):
#     t.color(color)
#     for _ in range(3):
#         t.forward(size)
#         t.left(120)

# # Function to draw a rectangle
# def draw_rectangle(width=90, height=90, color='brown'):
#     t.color(color)
#     for _ in range(2):
#         t.forward(width)
#         t.left(90)
#         t.forward(height)
#         t.left(90)

# # Function to draw a hexagon
# def draw_hexagon(size=60, color="pink"):
#     t.color(color)
#     for _ in range(6):
#         t.forward(size)
#         t.left(60)

# # Example usage
# t.penup()
# t.goto(-100, 100)
# t.pendown()
# draw_triangle()

# t.penup()
# t.goto(0, 0)
# t.pendown()
# draw_rectangle()

# t.penup()
# t.goto(100, -100)
# t.pendown()
# draw_hexagon()

# # Keep the window open
# turtle.done()
import turtle

turtle.Screen().bgcolor("white")
turtle.screensize(1000,300)
turtle.title("Shapes")
board=turtle.Turtle()
board.speed('slow')
board.pencolor('blue')

for i in range(3):
    board.forward(200)
    board.left(120)
    i=i+1