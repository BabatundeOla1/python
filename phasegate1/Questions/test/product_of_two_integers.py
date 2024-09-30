def get_product(first_number, second_number):

	'''if not isinstance(first_number, (int, float)):
		raises ValueError("invalid" )'''

	product = 0

	for count in range(second_number):

		product = product + first_number

	return product
		


