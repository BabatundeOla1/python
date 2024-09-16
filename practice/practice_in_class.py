balance = 0 

user_input = input("Enter option 1 to deposit or 2 to withdraw: ")

if user_input == 1:

	while True:
		user_input = float(input("Enter option 1 to deposit or 2 to withdraw: "))

		balance +=  user_input

if user_input == 2:

	amount = float(input("How much do you want to be deposited? "))

	if amount > balance:
		print("insufficient amount")

	else:
		balance = balance - amount


print("Current balance is: ", balance)