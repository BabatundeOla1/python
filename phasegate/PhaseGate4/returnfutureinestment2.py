'''
principal = float(input("Enter investment amount"))
annual_interest = float(input("Enter annual interest rate: "))
years_of_investment = int(input("Enter year(s) of investment"))
'''

print("year","\t","roi","\t", " ", "amount")

def return_future_investment(amount, rate, year):
	
	PERCENTAGE = 100
	annual_interest = rate / PERCENTAGE


	for count in range(1, year + 1):

		interest = rate * amount
		newbalance = amount + interest
		amount = newbalance
	
		print(f" {count}\t{interest:,.2f}\t{amount:,.2f}")


return_future_investment(10, 10, 10)