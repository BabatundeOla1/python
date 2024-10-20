def get_descending(elements):

	multiple = 1

	for counter in range(0, len(elements)):

		if counter % 2 != 0:

			multiple *= elements[counter]

	print(counter)





list_numbers = [3,1,2,7,4,6,5]
get_descending(list_numbers)
