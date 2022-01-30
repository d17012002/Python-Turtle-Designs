import turtle

pointer = turtle.Turtle()
pointer.getscreen().bgcolor("black")
pointer.pensize(2)

pointer.speed(4)

for i in range (6):
    for colors in ["red", "blue", "cyan", "magenta", "green", "yellow", "white"]:
        pointer.color(colors)
        pointer.circle(120, 90)     # pointer.circle(radius, angle)
        pointer.left(120)

turtle.done()