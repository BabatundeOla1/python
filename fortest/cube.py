def get_cube(number):
	
	if number < 0:
		raise ValueError("Invalid number")
	
	return number**3