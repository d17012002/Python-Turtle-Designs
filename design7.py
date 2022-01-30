import turtle
pointer = turtle.Turtle()

pointer.getscreen().bgcolor("black")
pointer.color("grey")
pointer.pensize(1)
pointer.speed(0)


for i in range (75):
    for i in range(4):
        pointer.forward(80)
        pointer.right(90)
    pointer.right(5)

for i in range(200):
    pointer.color("#363636")
    pointer.forward(350)
    pointer.left(169)

turtle.done()