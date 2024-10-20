try:
	rows = int(input("Enter numbers row: "))

	columns = int(input("Enter numbers columns: "))

	if rows > 0 and columns > 0:

		zeros = [[0]* columns] *rows

		for row in range(len(zeros)):

			for column in range(len(zeros[row])):

				zeros[row][column] += (row * column)

				print(f" {zeros[row][column]} \t", end = " ")
			print()



	else:
		print("ABEG NO BREAK ME BOSS!!")

except:
	print("LOL! OGA GO SIT DOWN JOR")