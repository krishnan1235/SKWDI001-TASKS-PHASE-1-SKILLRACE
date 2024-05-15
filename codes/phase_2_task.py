import turtle as t
a=t.Turtle()
a.speed(5) 
a.penup()
a.goto(-170,40)
a.pendown()
a.begin_fill()
#upper box
a.color("orange")
a.forward(350)
a.left(90)
a.forward(60)
a.left(90)
a.forward(350)
a.left(90)
a.forward(60)
a.end_fill()
#white box
a.color("white")
a.forward(60)
a.left(90)
a.forward(350)
a.left(90)
a.forward(60)
a.left(90)
a.forward(350)
a.end_fill()
#green box
a.left(90)
a.forward(60)
a.begin_fill()
a.color("green")
a.forward(60)
a.left(90)
a.forward(350)
a.left(90)
a.forward(60)
a.left(90)
a.forward(350)
a.end_fill()
#circle
a.color("navy")
a.penup()
a.goto(8,39)
a.pendown()
a.begin_fill()
a.circle(28)
a.penup()
a.goto(8,36)
a.pendown()
a.end_fill()
#big white
a.begin_fill()
a.color("white")
a.circle(25)
a.end_fill()
#small
a.goto(11,-13)
a.color("navy")
for i in range(24):
  a.begin_fill()
  a.circle(1)
  a.end_fill()
  a.penup()
  a.forward(6.1)
  a.right(14.6)
  a.pendown()
#inside circle
a.penup()
a.goto(9,13)
a.pendown()
a.begin_fill()
a.circle(3)
a.end_fill()
a.goto(9,10)
#spoke
for i in range(24):
  a.forward(25)
  a.back(25)
  a.right(15)
a.hideturtle()
