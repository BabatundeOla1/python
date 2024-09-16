def future_investment_value(investment_amount, monthly_interestRate, years):


	if investment_amount < 0 and monthly_interestRate < 0 and years < 0:
		raise ValueError("Input can not be negative!") 
	
	MONTHS_IN_YEAR = 12
	
	number_of_months = years * MONTHS_IN_YEAR

	monthly_interest_rate = monthly_interestRate / (100 * MONTHS_IN_YEAR)
	
	future_investment = investment_amount * ((1 + monthly_interest_rate) **number_of_months)
    
	return round(future_investment, 2)

	 