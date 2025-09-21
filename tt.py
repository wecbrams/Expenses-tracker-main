# import turtle 
# t = turtle.Turtle()
# s = turtle.Screen()
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
# s.bgcolor('black') 
# t.speed('fastest')
# t.hideturtle()
# while True:
#   for x in range(200): 
#     t.pencolor(colors[x%len(colors)])
#     t.width(x\100 + 1)
#     t.forward(x) 
#     t.left(59)
#   t.right(239)  
#   for x in range(200, 0, -1): 
#     t.pencolor('black') 
#     t.width(x\100 + 7)
#     t.forward(x) 
#     t.right(59) 
import turtle

t = turtle.Turtle()
s=turtle.Screen()

s.bgcolor("white")
t.fillcolor("red")
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.forward(200)
t.pendown()

for i in range(4):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)

t.penup()
t.backward(400)
t.pendown()

for i in range(6):
    t.forward(100)
    t.right(60)

turtle.done()