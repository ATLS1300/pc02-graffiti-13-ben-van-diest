#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
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
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
Turtle()
turtle = Turtle()
turtle.penup()
turtle.left(90)
turtle.forward(170)
turtle.pencolor("red")
turtle.pendown()
for i in range(10): 
    turtle.forward(50) 
    turtle.right(144) 
    
turtle.penup()
turtle.left(90)
turtle.forward(300)
turtle.pencolor("black")
turtle.pendown()
turtle.pensize(4)
turtle.circle(30)
turtle.penup()
turtle.forward(10)
turtle.right(120)
turtle.pendown()
turtle.forward(80)
turtle.penup()
turtle.right(130)
turtle.forward(120)


turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.right(230)
turtle.forward(50)
turtle.pendown()
turtle.forward(80)
turtle.penup()
turtle.right(130)
turtle.forward(120)

turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.right(230)
turtle.forward(50)
turtle.pendown()
turtle.forward(80)
turtle.penup()
turtle.right(130)
turtle.forward(120)

