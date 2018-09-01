"""
Console application for banking
	Authors:Achyuth Koneri V <achyuthkv@gmail.com>

"""

import random #import random library
class Bank:
	"""
	Class for bank accounts
	"""

	def __init__(self,name,password,amount=0):

		"""
		Constructor for class Bank
		Executed to create a instance of class
		Attributes:
		1.name = Account holder name
		2.password = pin for account
		3.balance = To keep track of oustanding account balance
		4.account_no = Account number assigned randomly to each instance
		5.statement = To keep track of all the transactions made ny account holder
		"""
		self.name = name
		self.password=password
		self.balance=amount
		self.account_no=random.randint(0,500) #randomly chooses a number in the range of 0 and 500
		self.statement=[]

	def withdraw(self,amount=0):
		"""
		Function to withdraw amount passed to parameters
		params : 
		1.amount = specifies the amount to be withdrawn 
		"""
		if self.balance >= amount+3000: # checks for minimum balance (3000)
			self.balance -= amount # if true withdraws money from account
			operation="withdraw"
			transc_list=[]
			transc_list.append(f"+{amount}")
			transc_list.append(self.balance)
			self.statement.append(transc_list) # appends tansaction and available balance to statement
		else:
			print("withdraw amount do not satisfy bank minimum balance limit")

	def deposit(self,amount=0):
		"""
		Function to deposit amount passed to parameters
		params : 
		1.amount = specifies the amount to be deposited 
		"""
		self.balance += amount
		operation="withdraw"
		transc_list=[]
		transc_list.append(f"+{amount}")
		transc_list.append(self.balance)
		self.statement.append(transc_list)




