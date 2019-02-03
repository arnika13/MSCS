# -*- coding: utf-8 -*-
'''
File: shapes.py
Date: 09/20/2016
Author: Prof. Nguyen Thai
Course: CSC 7014
Instructor: Prof. Nguyen Thai
Description: 'A simple program to introduce turtle graphics'
'''
import turtle
#setup the screen

turtle.setup(800,300) 

screen = turtle.Screen() # instantiate the screen class

screen.bgcolor("White")
screen.title("Draw circle")
turtle.penup()
turtle.color("green")
turtle.goto(-20,110)
turtle.write("Cool Colorful Shapes",align="center", font=("Arial",14,"bold"))
#create a cursor

cursor = turtle.Turtle()
cursor.pensize(3)

# Draw Traiangle


cursor.penup()
cursor.goto(-280,0)
cursor.pendown()
cursor.color("Red")
cursor.begin_fill()
cursor.color("Red")
cursor.circle(40, steps=3)
cursor.end_fill()
cursor.penup()
cursor.goto(-300,-50)
cursor.write("Triangle", font=("Times",12, "bold"))

# Draw Circle

cursor.penup()
cursor.goto(-120,0)
cursor.pendown()
cursor.color("Purple")
cursor.begin_fill()
cursor.color("purple")
cursor.circle(40)
cursor.end_fill()
cursor.penup()
cursor.goto(-140, -50)
turtle.fillcolor("purple")
turtle.end_fill()
cursor.write("Circle", font=("Times",12, "bold"))

#Draw Square

cursor.penup()
cursor.goto(20,0)
cursor.pendown()
cursor.color("navy")
cursor.begin_fill()
cursor.color("navy")
cursor.circle(40, steps=4)
cursor.end_fill()
cursor.penup()
cursor.goto(0,-50)
cursor.write("Square", font=("times", 12,"bold"))

#Draw Pentagon

cursor.penup()
cursor.goto(150,0)
cursor.pendown()
cursor.color("green")
cursor.begin_fill()
cursor.color("green")
cursor.circle(40, steps=5)
cursor.end_fill()
cursor.penup()
cursor.goto(130,-50)
cursor.write("Pentagon", font=("times", 12,"bold"))

# Draw Hexagon

cursor.penup()
cursor.goto(270,0)
cursor.pendown()
cursor.color("yellow")
cursor.begin_fill()
cursor.color("yellow")
cursor.circle(40, steps=6)
cursor.end_fill()
cursor.penup()
cursor.goto(250,-50)
cursor.write("Hexagon", font=("times", 12,"bold"))

cursor.hideturtle()
turtle.done()
