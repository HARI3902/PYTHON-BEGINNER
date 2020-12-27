import turtle
turtle=turtle.Turtle()
turtle.speed(0)
def square():
    for i in range(3):
        turtle.forward(100)
        turtle.left(90)

def second():
    for i in range(4):
        square()
        turtle.forward(100)

for i in range(3):
    second()
    turtle.forward(100)
