import sys
import turtle
import time

# setup the window and the turtle
window = turtle.Screen()
window.setup(600, 600)
t = turtle.Turtle()
t.speed(10)
# get input from the user
num_squares = int(sys.argv[1])
side_length = int(sys.argv[2])

# draw the flower consisting of num_squares squares
# each square is side_length long
# TODO: write the code using at least 1 for loop!
angle= 360/ num_squares
for i in range (num_squares):
    for i in range(4):
        t.forward(side_length)
        t.left(90)
    t.right(125)
    
window.exitonclick()