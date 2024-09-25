a_list = []

even_index = 0

for numbers in range(0, 6):
	a_list += [numbers]
	
	if a_list[numbers] % 2 != 0:
		even_index = a_list[numbers]

		print(even_index)