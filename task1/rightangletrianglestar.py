userinput = int(input("Enter the number of lines: "))

for row in range(0, userinput+1):

	print(" ")
	
	for column in range(0, row):

			print("*", end = " ")