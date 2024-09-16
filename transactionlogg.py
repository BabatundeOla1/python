def make_withdraw():

	print("Withraw>>>\n")

	balance = 1000
		
	withdraw = float(input("Enter amount to be withdrawn: "))

	if withdraw > balance:
		print("Insufficient balance!")

	if withdraw <= 0:
		print("Error!!")

	if withdraw <= -1:
		print("THANK YOU FOR BANKING WITH US!")

	if withdraw < balance:
		balance -= withdraw

		print(balance)

	mainmenu()




def make_deposit():

	balance = 0

	total_deposit = 0

	print("Deposit>>>\n")

	while True:
		deposit = float(input("Enter amount to be deposited and (-1 to the menu): "))
		balance +=  deposit

		if deposit <= -1: 
			print(f'your total sum of money is {balance}')
			
			break
	mainmenu()
		

def check_balance():

	print("Balance>>>\n")

	balance = 0
	
	total_balance = make_deposit() - make_withdraw()

	print(f'Your Total Balance is= {total_balance}')









def mainmenu():

	menu = """ 
		WELCOME TO SWIFT BANK.
		--------------------
		1 >>> Deposit.
		2 >>> Withdrawal.
		3 >>> Balance.
		4 >>> Exit.
		--------------------

	"""
	print(menu)

mainmenu()

choice = input("enter a number: ")

match choice:

	case "1" :
		make_deposit()

	case"2" :
		make_withdraw()

	case'3' :
		check_balance()
	

	case'4' :
		print("Exit.")
