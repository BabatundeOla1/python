principal = float(input("Enter principal amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
duration = int(input("Enter duration: "))

PERCENTAGE = 100
annual_interest = annual_interest_rate / PERCENTAGE

print("year","\t","roi","\t", " ", "amount")

for year in range(1, duration + 1):

	interest = annual_interest * principal
	newbalance = principal + interest
	principal = newbalance

	print(f" {year}\t{interest:,.2f}\t{principal:,.2f}")













