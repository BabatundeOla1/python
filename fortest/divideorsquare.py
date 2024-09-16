"""
create a function name divide_or_square that takes number as parameter
check if number is divisible by 5 and return its square root 
to find square root, power number with exponential 0.5
if number divisible by 5 has a remainder,
return its remainder
"""

def divide_or_square(number):

	if number < 0:
		raise ValueError("Invalid number")

	if number % 5 == 0:
		squareroot = number ** 0.5

		return squareroot

	if number % 5 != 0:
		
		return number % 5

	

	