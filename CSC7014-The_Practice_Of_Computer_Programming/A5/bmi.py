"""
File: bmi.py
Date: 10/14/2016
Author: Arnika Vishwakarma
Course: CSC 7014
Instructor: Prof. Nguyen Thai
Description: 'A program to implement the body mass index(BMI) class'
"""

# Created Class

class BMI:     
    
    # defining initializer method
    
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
   
    # defined function getBMI
   
    def getBMI(self):
       kilogram_per_pound= 0.453
       meters_per_foot= 0.3048
       bmi= (self.weight * kilogram_per_pound)/((self.height*meters_per_foot)**2)
       return format(bmi,'.2f')
       
    
    # defined getStatus method 
    
    def getStatus(self):
        if self.age < 16:
            return "Invalid age: Please enter the age 16 or above"
        else:    
            bmi=float(self.getBMI())
            if bmi <= 18.5:       
                return "Underweight"
            elif bmi <=24.9:
                return "Normal"
            elif bmi<= 29.9:
                return "Overweight"
            else:
                return "Obese"
          
    
      
   
