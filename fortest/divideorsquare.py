def divide_or_square(number):

	if number < 0:
		raise ValueError("Invalid number")

	if number % 5 == 0:
		 return number ** 0.5

	if number % 5 != 0:
		
		return number % 5

	

	