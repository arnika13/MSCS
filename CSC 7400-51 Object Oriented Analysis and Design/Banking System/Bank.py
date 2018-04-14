"""
File: Bank.py
Date: 04/09/2017
Author: Arnika Vishwakarma
Course: CSC 7400-51
Instructor: Prof. Nguyen Thai
Description: 'Banking system implementation using facade pattern'
"""
# Welcome Bank subclass


class WelcomeToBank(object):
	def __init__(self):
		print("Welcome to Banking System \n")
        
		
        

# Account number check subclass

class AccountNumberCheck(object):
	def __init__(self):
		self._accountNumber = 12345678

	def getAccountNumber(self):
		return self._accountNumber

	def accountActive(self, acctNumToCheck):
		if acctNumToCheck == self.getAccountNumber():
			return True
		else:
			return False
   
# Security code check subclass

class SecurityCodeCheck(object):
	def __init__(self):
		self._securityCode = 1234

	def getSecurityCode(self):
		return self._securityCode

	def isCodeCorrect(self, secCodeToCheck):
		if secCodeToCheck == self.getSecurityCode():
			return True
		else:
			return False
   
# Funds Check subclass
			
class FundsCheck(object):
	def __init__(self):
		self._cashInAccount = 1000.00

	def getCashInAccount(self):
		return self._cashInAccount

	def decreaseCashInAccount(self, cashWithdrawn):
		self._cashInAccount -= cashWithdrawn

	def increaseCashInAccount(self, cashDeposited):
		self._cashInAccount += cashDeposited

	def haveEnoughMoney(self, cashToWithdrawal):
		if cashToWithdrawal > self.getCashInAccount():
			print("Error: You don't have enough money to withdraw")
			print("Current Balance is : " + str(self.getCashInAccount()))
			return False
		else:
			self.decreaseCashInAccount(cashToWithdrawal)
			print("Withdrawal Complete.\nCurrent Balance is :" + str(self.getCashInAccount()))
			return True

	def makeDeposit(self, cashToDeposit):
		self.increaseCashInAccount(cashToDeposit)
		print("Deposit Complete.\nCurrent Balance is : " + str(self.getCashInAccount()))
		
#Facade Class
		
class BankAccountFacade(object):
    def __init__(self, newAcctNum, newSecCode):
        self._accountNumber = newAcctNum
        self._securityCode = newSecCode
        self._bankWelcome = WelcomeToBank()
        self._acctChecker = AccountNumberCheck()
        self._codeChecker = SecurityCodeCheck()
        self._fundChecker = FundsCheck()
        
    def getAccountNumber(self):
        return self._accountNumber
    def getSecurityCode(self):
        return self._securityCode
    def withdrawCash(self, cashToGet):
        if self._acctChecker.accountActive(self.getAccountNumber()) and self._codeChecker.isCodeCorrect(self.getSecurityCode()):
            self._fundChecker.haveEnoughMoney(cashToGet)
            print("Transaction Complete\n")
        else:
            print("Incorrect Account Number and/or Security Code\n")
    def depositCash(self, cashToDeposit):
        
        if self._acctChecker.accountActive(self.getAccountNumber()) and self._codeChecker.isCodeCorrect(self.getSecurityCode()):
            self._fundChecker.makeDeposit(cashToDeposit)
            print("Transaction Complete\n")
        else:
            print("Incorrect Account Number and/or Security Code\n")
    def checkAccountBalance(self):
           if self._acctChecker.accountActive(self.getAccountNumber()) and self._codeChecker.isCodeCorrect(self.getSecurityCode()):
                a=self._fundChecker.getCashInAccount()
                print(" Account Balance amount is : ",a)
                
           else:
                print("Incorrect Account Number and/or Security Code\n")
                
