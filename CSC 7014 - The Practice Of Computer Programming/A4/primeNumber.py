"""
File: primeNumber.py
Date: 10/07/2016
Author: Arnika Vishwakarma
Course: CSC 7014
Instructor: Prof. Nguyen Thai
Description: 'A program to verify whether a given integer number is a prime number'
"""

# Defining function

def isPrime(number):
    if number>1: # Using if statement to check if the number is greater than 1 or not
        for i in range(2,number):  #Initializing for loop 
            if (number % i == 0):  # using if statement to check the condition 
                return False  #return false if the the number is not prime
        return True            # Return True if the number is prime
    else:
        return False


# Test Function to test isPrime

def testPrime(number, expectedResult):  # Creating another function named testPrime
    actualResult = isPrime(number)
    if(actualResult == expectedResult): # Calling isPrime function
        print("Input number ", number ," - Test Passed, isPrime() = ", actualResult)
    else:
        print("Input number ", number, " - Test Failed, isPrime() = ", actualResult, ", Expected = ", expectedResult)



# Test Cases

testPrime(21,  False)  # Call testPrime() by passing the arguments
testPrime(29,  True)
testPrime(109, True)
testPrime(163, True)
testPrime(227, True)


