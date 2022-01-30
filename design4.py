import turtle
pointer = turtle.Turtle()

pointer.speed(9)

pointer.color("black", "yellow")
pointer.begin_fill()

for i in range (80):
    pointer.forward(150)
    pointer.left(149)

pointer.end_fill()
turtle.done()