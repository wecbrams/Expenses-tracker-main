import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Spiral pattern")
mPen=turtle.Turtle()
size =0
while True:
    for i in range(4):
        mPen.fd(size+1)
        mPen.left(90)
        size = size -5
    size = size +1
    

