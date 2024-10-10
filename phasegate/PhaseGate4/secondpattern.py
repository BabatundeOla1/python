for column in range(5):
	print(" ")
	
	for row in range(1, column + 2):
		if row % 2 == 0:
			print("*", end = " ")
		else:
			print(row, end = " ")


for column2 in range(5, 1, -1 ):
	print(" ")
	
	for row2 in range(1, column2 + 1):
		if row2 % 2 == 0:
			print("*", end = " ")
		else:
			print(row2, end = " ")
