import turtle

pointer = turtle.Turtle()
pointer.getscreen().bgcolor("black")
pointer.pensize(2)

pointer.speed(0)

for i in range (6):
    for colors in ["red", "blue", "cyan", "magenta", "green", "yellow", "white"]:
        pointer.color(colors)
        pointer.circle(100)
        pointer.left(10)

turtle.done()