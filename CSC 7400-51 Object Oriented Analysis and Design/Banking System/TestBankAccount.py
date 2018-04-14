
"""
File: TestBankAccount.py
Date: 04/09/2017
Author: Arnika Vishwakarma
Course: CSC 7400-51
Instructor: Prof. Nguyen Thai
Description: 'Implementing a class to test facade interactively'
"""
from Bank import BankAccountFacade

import sys

class TestBankAccount(object):
    accessingBank = BankAccountFacade(12345678, 1234)
  
    AcNum=int(input("Enter the account number: \n \n"))
    if (AcNum == accessingBank.getAccountNumber()):
        print("You have entered the correct Account Number ")
    
    SC= int(input("Enter the Security Code : \n"))
    if (SC== accessingBank.getSecurityCode()):    
        print("You have entered the correct Security code")
        choice = 1    
        while(True):
            choice=int(input(" Please Choose the Options : \n\n 1. Check your Balance \n 2. Withdraw Cash \n 3. Deposit cash \n 4. Exit the system \n"))
            if(choice == 1):
                accessingBank.checkAccountBalance()
            elif(choice == 2):
                amount=float(input("Enter the amount to withdraw : "))
                accessingBank.withdrawCash(amount)
            elif(choice == 3):
                deposit=float(input("Enter the amount to deposit : "))
                accessingBank.depositCash(deposit)
            elif(choice == 4):
                print("Thank you for banking with us !!")
                sys.exit()
            else:
                print("Invalid Input. Try again !!")
    else:
        print("Please enter the correct account number and Security Code")