principal = float(input("Enter principal amount: "))

annual_interest_rate = float(input("Enter annual interest rate: "))

duration = int(input("Enter duration: "))

PERCENTAGE = 100

print("year","\t","roi","\t", " ", "amount")

for count in range(duration):

	interest = annual_interest_rate / PERCENTAGE

	amount = principal * interest

	yearly_return = principal + amount

	
	print(count, "\t",amount, "\t", yearly_return)






