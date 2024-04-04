import turtle

mikey = turtle.Turtle()
raph = turtle.Turtle()

for i in range(4):
    mikey.forward(100)
    mikey.right(90)

raph.penup()
raph.right(360)
raph.forward(180)
raph.pendown()
for i in range(3):
    raph.forward(80)
    raph.left(120)

