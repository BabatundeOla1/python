def future_investment_value(investment_amount, monthly_interest_rate, years):

    MONTHS_IN_YEAR = 12

    number_of_months = years * MONTHS_IN_YEAR

    monthly_interest_rates = monthly_interest_rate / (100 * MONTHS_IN_YEAR)

    future_investment = investment_amount * ((1 + monthly_interest_rates) ** number_of_months)
    return future_investment

print(future_investment_value(500, 50, 3))   