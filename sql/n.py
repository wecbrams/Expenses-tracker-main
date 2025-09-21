import turtle

# Setup turtle and screen
t = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor('lightblue')
sc.setup(500, 600)

# Triangle drawing function
def draw_triangle(size=200, color="blue"):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Rectangle drawing function
def draw_rectangle(width=129, height=90, color='brown'):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Hexagon drawing function
def draw_hexagon(size=100, color="pink"):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(size)
        t.left(60)
    t.end_fill()

# Example usage
t.penup()
t.goto(-100, 0)
t.pendown()
draw_triangle()

t.penup()
t.goto(100, 0)
t.pendown()
draw_rectangle()

t.penup()
t.goto(0, -150)
t.pendown()
draw_hexagon()

t.hideturtle()
turtle.done()
