
"""
File: palindrome.py
Date: 10/21/2016
Author: Arnika Vishwakarma
Course: CSC 7014
Instructor: Prof. Nguyen Thai
Description: 'A program to implement the checking of a palindrome string'
"""

# Defined function 

def isPalindrome(s):
       
        s=s.lower()      # convert the string to lowercase
        s = s.replace(" ","")    #Eliminate White Spaces
        rev_s= s[::-1]
        if (s== rev_s):
            return True    # Returns true if the string is palindrome
        else:
            return False  # Returns false if the string is not palindrome
        

# Test function

def testPalindrome(s, expectedResult):
    actualResult = isPalindrome(s)
    if(actualResult == expectedResult):
        print("Test Passed : ", actualResult)
    else:
        print("Test Failed : ActualResult = ", actualResult, " ExpectedResult = ", expectedResult)


#Test Cases
 
testPalindrome("madam",True)
testPalindrome("moon",False)
testPalindrome("Was it a cat I saw",True)

