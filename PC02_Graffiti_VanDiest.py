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
from turtle import * 

colormode(255)


panel = Screen()
w = 750 
h = 750 
panel.setup(width=w, height=h) 

image = "Bezos.gif"
panel.bgcolor("black")
panel.bgpic(image)

up()

goto(-22,112)
shape("circle")
shapesize(2,2.6,1)
left(12)
stamp()

goto(47,120)
stamp()

goto(11,125)
shape("square")
shapesize(.8,5.7,1)
right(4)
stamp()

goto(-45,122)
shape("circle")
shapesize(.5,.5,1)
down()
pensize(7)

backward(45)
right(164)
forward(10)

up()
color(175,0,0)
goto(47,120)
stamp()

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






