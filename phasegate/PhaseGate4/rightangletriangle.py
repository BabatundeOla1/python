for column in range(5):
	print(" ")

	
	for row in range(1, column + 2):

		if row % 2 == 0:
			print("*", end = " ")
		else:
			print(row, end = " ")


