import turtle
pointer = turtle.Turtle()

pointer.speed(2)
pointer.color("black", "yellow")  # you can also put color hash color; Black -> pointer color, Yellow -> fill color

pointer.begin_fill()
for j in range (5):
  for i in range (4):
    pointer.forward(50)
    pointer.left(90)

  pointer.forward(50)
pointer.end_fill()

turtle.done()