'''
File: testBmi.py
Date: 10/14/2016
Author: Arnika Vishwakarma
Course: CSC 7014
Instructor: Prof. Nguyen Thai
Description: 'A program to test the BMI class'
'''
from bmi import BMI
 
 # defined healthStatus method with parameters
 
def healthStatus(name,age,weight,height):
    bmiObj= BMI(name,age,weight,height)  # created object of class BMI
    return bmiObj.getStatus()

# test Cases

status = healthStatus("John",18,165,5.9)
print("Health status of John is:", status)
status = healthStatus("Mary",25,115,5.2)
print("Health status of Mary is : ", status)
status = healthStatus("Mark",60,135,5.6)
print("Health status of Mark is : ", status)



