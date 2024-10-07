main_menu = """ 	   Marital Status 
-------------------------
0 -> single

1 -> Married

2 -> separate

3 -> Head of house

-------------------------
	Enter a number:
"""

input(main_menu)

userinput = int(input("Enter number for marital status: "))

tax = 0

PERCENTAGE = 100

if userinput == 0:
	
	print("Single")

	amount = int(input("Enter Taxable income: "))

	if (amount > 0 and amount <= 8350):
		tax = amount * (10 / 100)

	elif amount > 8351 and amount <= 33950:
		tax = amount * (15 / 100)

	elif amount > 33951 and amount <= 82250:
		tax = amount * (25 / 100)

	elif amount > 82251 and amount <= 171550:
		tax = amount * (28 / 100)

	elif amount > 171551 and amount <= 372950:
		tax = amount * (33 / 100)

	elif amount >= 372951:
		tax = amount * (35 / 100)

print(tax)
		