"""
Console application for banking
	Authors:Achyuth Koneri V <achyuthkv@gmail.com>

"""
from bankprob import Bank  # import class bank from bankprob.py
from tabulate import tabulate #import tabulate library to display in table on console


"""
** variables**
accounts (dict) {account_no: Bank Object} holds all the accounts created during the session.
"""
accounts={}
while(True):
	headers=["option","operation"] 
	"""
	print options in a table
	"""
	table=[[1,"Create account"],[2,"Withdraw"],[3,"deposit"],[4,"Check Statement"]]
	print(tabulate(table, headers, tablefmt="grid"))
	choice=int(input())
	if choice==1:
		name=input("enter name :")
		password=int(input("enter password:"))
		user=Bank(name,password)
		accounts[int(user.account_no)]=user 
		"""
		After creating an account display the account number to the user
		"""
		print(f"your account number is {user.account_no}")


	elif choice==2:
		"""
		Get the account details from the user
		"""
		account_no=int(input("enter the account number"))
		password=int(input("enter password"))

		if accounts[account_no].password==password:
			amount=int(input("enter the amount to with draw"))
			accounts[account_no].withdraw(amount) #withdraw the sepecified amount by making a call to withdraw function of class bank
		else:
			print("wrong credentials")

	elif choice==3:
		"""
		Get the account details from the user
		"""
		account_no=int(input("enter the account number"))
		password=int(input("enter password"))
		if accounts[account_no].password==password:
			amount=int(input("enter the amount to deposit")) #deposit the sepecified amount by making a call to deposit function of class bank
			accounts[account_no].deposit(amount)
		else:
			print("wrong credentials")
		

	else:
		"""
		Get the account details from the user
		"""
		account_no=int(input("enter the account number"))
		password=int(input("enter password"))
		printdata=[]
		table=["transaction","balance"]
		"""
		Display the statement consiting of all the trasactions of the user in tabular form
		"""
		if accounts[account_no].password==password:
			printdata=accounts[account_no].statement
			print(tabulate(printdata, table, tablefmt="grid"))

		else:
			print("wrong credentials")


