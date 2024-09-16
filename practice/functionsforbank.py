def make_deposit(deposit):

	balance = 0
		deposit = float(input("Enter amount to be deposited(-1 to end): "))

		balance += deposit

		if deposit == -1:
			break

		return balance

make_deposit()


















'''def mainmenu():

	menu = """ 
		WELCOME TO SWIFT BANK.
		--------------------
		1 >>> Deposit.
		2 >>> Withdrawal.
		3 >>> Balance.
		4 >>> Exit.
		--------------------

	"""

choice = input(menu)

match choice:
'''
		