total_deposit = 0

balance = 0

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

	case'1' : 
		print("Deposit.")

		while True:

			deposit = float(input("Enter amount to be deposited: "))

			if deposit == -1:
				print("THANK YOU FOR BANKING WITH US!", menu)
				break

			total_deposit +=  deposit

	case'2' :
		
		print("Withraw.")
		
		withdraw = float(input("Enter amount to be withdrawn: "))

		if withdraw > total_deposit:
			print("Insufficient balance!")

		if withdraw == -0:
			print("Error!!")

		if withdraw == -1:
			print("THANK YOU FOR BANKING WITH US!", menu)
			
	case'3' :
		print("Balance.")

		balance = total_deposit - withdraw

		print("Your Balance:$",balance)

	case'4' :
		print("Exit.")
