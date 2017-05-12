import os

class BankAccount(object):
	
	def __init__(self, initial_balance=0)
		self.balance = initial_balance
		
	def deposit(self, amount):
			self.balance += amount
			
	def withdraw(self, amount):
			self.balance -= amount
			
	def overdrawn(self):
			return self.balance < 0
		
class Controller():
	
	def mainLoop(self):
			while self.should_run == True:
				self.drawScreen()
				self.handleInput()
				self.mainLoop()
				
class View():
	
	
	
	