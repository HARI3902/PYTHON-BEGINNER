import turtle
turtle = turtle.Turtle()
turtle.speed(0)
def circle():
  for i in range(4):
    turtle.forward(100)
    turtle.left(90)

for i in range(200):
    circle()    
    turtle.right(11)
