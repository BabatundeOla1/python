list = [1, 2, 3, 4, 5, 6]

def get_swap(array):

	for count in range(1, len(array), 2):

		if count % 2 != 0:
			temp = array[count]
			array[count] = array[count-1]
			array[count-1] = temp

	return(array)


print(get_swap(list))


