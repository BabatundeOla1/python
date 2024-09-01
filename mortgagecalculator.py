"""
prompt user to enter principal
prompt user to enter annual interest rate
prompt user to enter duration
convert annual interest rate to monthly interest rate
convert duration to month
calculate for the monthly monthly payment 
"""


principal = float(input("Enter principal amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
duration = int(input("Enter duration: "))


PERCENTAGE = 100

MONTHSINYEAR = 12

monthly_interest_rate = annualinterestrate // PERCENTAGE

duration_in_months = duration * MONTHSINYEAR 

first_step = monthly_interest_rate * ((1 + monthly_interest_rate) ** duration_in_months)

second_step = ((1 + monthly_interest_rate) ** duration_in_months) - 1

monthly_payment = principal * (first_step / second_step)

print("Monthly Payment is $", round(monthly_payment, 2))