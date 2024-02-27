import sys
import turtle

# setup the window and the turtle
window = turtle.Screen()
window.setup(600, 600)
t = turtle.Turtle()
t.speed(10)
# get input from the user
num_points = int(sys.argv[1])
side_length = int(sys.argv[2])
t.up()
t.goto(0,250)
t.right(60)
t.forward(side_length)
t.down()
angle = 360 // num_points
for i in range(num_points):
    t.left(60)
    t.forward(side_length)
    t.right(120)
    t.forward(side_length)
    t.right(120)
    t.left(180-angle)

window.exitonclick()