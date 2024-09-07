userinput = int(input("Enter the number of lines: "))

for row in range(1, userinput + 1):

	print(" ")
	
	for column in range(1, row + 1):

		print(column, end = " ")

for row in range(0, userinput, -1):

	print(" ")
	
	for column in range(row, 0, -1):

		print(column, end = " ")


