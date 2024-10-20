def get_descending(elements):

	for counter in range(len(elements)):

		for counts in range(1, len(elements)):

			if elements[counter] < elements[counts - 1]:

				swap = elements[counter]
				elements[counter] = elements[counts - 1]
				elements[counts - 1] = swap
	
	print(elements)






list_numbers = [3,1,2,7,4,6,5]
get_descending(list_numbers)