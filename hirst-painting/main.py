import turtle
from turtle import Turtle, Screen
import random
colors = [(238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

def print_dot(how_much_x,how_much_y,size_of_dot,space_between,turtle):

    size_of_dot = size_of_dot
    space_between = space_between

    for i in range(how_much_y):
        turtle.setposition(-500,turtle.ycor()+2*size_of_dot+space_between)
        for i in range(how_much_x):
            turtle.dot(size_of_dot)
            turtle.forward(2*size_of_dot+space_between)
            turtle.pencolor(random.choice(colors))

turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.setx(-500)
tim.sety(-450)


print_dot(10,10,20,50,tim)


screen = Screen()
screen.exitonclick()

