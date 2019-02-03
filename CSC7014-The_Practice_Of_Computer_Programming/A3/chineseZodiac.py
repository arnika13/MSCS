# -*- coding: utf-8 -*-
"""
File: chineseZodiac.py
Date: 09/29/2016
Author: Prof. Nguyen Thai
Course: CSC 7014
Instructor: Prof. Nguyen Thai
Description: 'To calculate the Chinese Zodiac for a given user input as a year number'
"""
import turtle # importing turtle


while(True):
    year=int(input("Enter the year:  "))
    if(year < 0):
        print("Invalid Input. Please enter a valid year !")
    else:
        break
    
birth_year = year % 12

#setup the screen
turtle.setup(800,300) 

screen = turtle.Screen() # instantiate the screen class

screen.bgcolor("White")
screen.title("ChineseZodiac")

turtle.penup()
turtle.color("Blue")
turtle.goto(-20,280)
turtle.write("Year to Chinese Zodiac Conversion",align="center", font=("Arial",16,"bold")) 

# Creating a cursor to draw circle

cursor = turtle.Turtle()
cursor.pensize(2)

# Drawing a circle

cursor.penup()
cursor.goto(-50,-150)
cursor.pendown()
cursor.color("Black")
cursor.circle(200)

# Drawing lines inside the circle

for i in range(0,12):    # initializing for loop that repeats twelve times
 cursor.goto(-50,50) 
 cursor.forward(200)
 cursor.right(30)
 
 # writing the Zodiac names inside the circle using list

animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep']
 
cursor.penup()
cursor.goto(-220,10)
cursor.color("Red" if birth_year==0 else "Blue")
cursor.write("monkey", font=("Arial",12,"bold"))

cursor.goto(-220,60)
cursor.color("Red" if birth_year==1 else "Blue")
cursor.write("rooster", font=("Arial",12,"bold"))

cursor.goto(-180,150)
cursor.color("Red" if birth_year==2 else "Blue")
cursor.write("dog", font=("Arial",12,"bold"))

cursor.goto(-100,190)
cursor.color("Red" if birth_year==3 else "Blue")
cursor.write("pig", font=("Arial",12,"bold"))

cursor.goto(-20,190)
cursor.color("Red" if birth_year==4 else "Blue")
cursor.write("rat", font=("Arial",12,"bold"))

cursor.goto(50,140)
cursor.color("Red" if birth_year==5 else "Blue")
cursor.write("ox", font=("Arial",12,"bold"))

cursor.goto(70,80)
cursor.color("Red" if birth_year==6 else "Blue")
cursor.write("tiger", font=("Arial",12,"bold"))

cursor.goto(60,10)
cursor.color("Red" if birth_year==7 else "Blue")
cursor.write("rabbit", font=("Arial",12,"bold"))

cursor.goto(50,-70)
cursor.color("Red" if birth_year==8 else "Blue")
cursor.write("dragon", font=("Arial",12,"bold"))

cursor.goto(-20,-120)
cursor.color("Red" if birth_year==9 else "Blue")
cursor.write("snake", font=("Arial",12,"bold"))

cursor.goto(-120,-120)
cursor.color("Red" if birth_year==10 else "Blue")
cursor.write("horse", font=("Arial",12,"bold"))

cursor.goto(-190,-70)
cursor.color("Red" if birth_year==11 else "Blue")
cursor.write("sheep", font=("Arial",12,"bold"))
# cursor.pendown()   
# Display the Zodiac year and animal     
   
cursor.goto(-30,-200)
cursor.color("Green")
stringToPrint = "Year " + str(year) + " is the " + animals[birth_year] + "!"
cursor.write(stringToPrint,align="center",font=("Arial",14,"bold"))

# closing turtle

cursor.hideturtle()
turtle.done()
