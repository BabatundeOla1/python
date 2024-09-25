prime


counts = 0

	for count in range(number):

		if number % count == 0:
			counts = counts + 1

		if counts == 2:
			
			return True

		else:
			return False



palindrome


reverse = 0

	while number != 0:
		
		reverse = reverse * 10 + (number % 10)

		number = number % 10

		if reverse == number:

			return reverse

		else:
			return False