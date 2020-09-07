#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Ben Van Diest
September 4, 2020
PC02 Bezos Terminator
'''
from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("black")
panel.bgpic(image)

up()

#left shade
goto(-22,112)
shape("circle")
shapesize(2,2.6,1)
left(12)
stamp()

#right shade
goto(47,120)
stamp()

#middle bar
goto(11,125)
shape("square")
shapesize(.8,5.7,1)
right(4)
stamp()

#side piece
goto(-45,122)
shape("circle")
shapesize(.5,.5,1)
down()
pensize(7)

backward(45)
right(164)
forward(10)

#red eye
up()
color(175,0,0)
goto(47,120)
stamp()

#red eye streaks
pensize(1.8)
color("red4")
down()
forward(20)
forward(-20)
left(45)
forward(20)
forward(-20)
left(45)
forward(20)
forward(-20)
left(45)
forward(20)
forward(-20)
left(45)
forward(20)
forward(-20)
left(45)
forward(20)
forward(-20)
left(45)
forward(20)
forward(-20)
left(45)
forward(20)
forward(-20)
up()

#thought bubbles
goto(85,70)
color("WhiteSmoke")
down()
circle(10)
up()

goto(130,130)
down()
circle(20)
up()

goto(270,350)
down()
circle(110)
up()

#money symbol
goto(290,300)
color("green4")
down()
pensize(15)
left(22)
forward(120)
left(90)
forward(50)
left(90)
forward(120)
right(90)
forward(50)
right(90)
forward(120)
up()

goto(205,320)
down()
left(90)
forward(140)
up()

goto(255,320)
down()
forward(140)
up()






