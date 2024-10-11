for numbers in range(1, 50 + 1):

	if numbers % 3 == 0 and numbers % 5 == 0:
		print("fizzbuzz")
		
	elif numbers % 3 == 0:
		print("fizz")

	elif numbers % 5 == 0:
		print("buzz")

	else:
		print(numbers)
	