import turtle
pointer = turtle.Turtle()

pointer.speed(4) 

pointer.color("black", "yellow")
pointer.begin_fill()

for j in range (5):
  for i in range (4):
    pointer.forward(50)
    pointer.left(90)

  pointer.forward(50)

pointer.end_fill()

pointer.penup()     #move pointer without drawing
pointer.left(90)
pointer.forward(150)
pointer.left(90)
pointer.pendown()

pointer.color("black", "red")
pointer.begin_fill()

for j in range (5):
  for i in range (4):
    pointer.forward(50)
    pointer.left(90)
  pointer.forward(50)

pointer.end_fill()
  

turtle.done()