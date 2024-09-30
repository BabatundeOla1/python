def even_position(numbers):

	for count in range(len(numbers)):
		if numbers[count] % 2 == 0:
		
			even_index = numbers[count]
			
			print(even_index)


list_numbers = [1, 2, 3, 4, 5, 6]
even_position(list_numbers)

