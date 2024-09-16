"""
initialize the amount to be deposited as zero
prompt user to enter amount deposited 
since we don't how many time the user would be depositing, we make use of the while loop 
calculate the total amount deposited by the user
initialize the withrawn amount to zero
initialize the total amount withdraw to zero 
since we don't how many time the user would be withdrawing, we make use of the while loop
calculate the total amount withdrawn by the user
create a variable net amount
subtract the total amount witdrawn from the total amount deposited
srore in the variable net amount  
display the net amount 

"""

total_amount_deposited = 0

deposit = 0

while deposit != -1:

	deposit = float(input("Enter amount to be deposited or -1 to quit: "))

	total_amount_deposited = total_amount_deposited + deposit



withdraw = 0

total_amount_withdrawn = 0

while withdraw != -1:

	withdraw = float(input("Enter amount to be withdrawn or -1 to quit: "))

	total_amount_withdrawn = total_amount_withdrawn + withdraw



net_amount = total_amount_deposited - total_amount_withdrawn
	
print("Net amount =", + net_amount)




if total_amount_withdrawn > total_amount_deposited:

	print("Insufficient funds, kindly deposit!")






