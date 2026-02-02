import turtle

turtle.Screen().bgcolor("lime")
board = turtle.Turtle()

#First triangle
board.forward(100) 

board.left(120)
board.forward(100) 

board.left(120)
board.forward(100) 

board.penup()
board.right(150)
board.forward(50) 

#Second Triangle
board.pendown()
board.right(90)
board.forward(100) 

board.right(120)
board.forward(100) 

board.right(120)
board.forward(100) 
turtle.done()