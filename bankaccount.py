total_deposit = 0

while True:

	deposit = float(input("Enter amount to be deposited (-1 to stop depositing): "))

	if deposit == -1:
		break

	total_deposit = total_deposit +  deposit

withdraw = float(input("Enter amount to be withdrawn: "))

if withdraw > total_deposit:
	print("Insufficient balance!")

if withdraw < 1:
	print("Error!")	

else:
	balance = total_deposit - withdraw

	print("Your Balance:$",balance)