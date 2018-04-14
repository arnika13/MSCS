
"""
File: TestBank.py
Date: 04/09/2017
Author: Arnika Vishwakarma
Course: CSC 7400-51
Instructor: Prof. Nguyen Thai
Description: 'Test cases for the Banking system'
"""
from Bank import BankAccountFacade

accessingBank = BankAccountFacade(12345678, 1234)

# Test Case 1
accessingBank.checkAccountBalance()
accessingBank.withdrawCash(50.0)
accessingBank.depositCash(100.0)

   
# Test Case 2
accessingBank = BankAccountFacade(123456238, 134)
accessingBank.withdrawCash(50.0)
accessingBank.depositCash(100.0)