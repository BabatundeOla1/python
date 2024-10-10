lists = [1, 3, 4, 7, 2, 6, 9, 5, 3, 8]
average = 0
sum = 0

def get_length(number):

	count = 0

	for numbers in list(number):

		count = count + 1
		
	return count

size = get_length(lists)



def get_even(number):

	evensum = 0

	for count in range(size):
	
		if (count % 2 == 0):
			evensum = evensum + count

	return evensum

get_even(lists)



def get_odd(number):

	oddsum = 0

	for count in range(size):

		if(count % 2 != 0):

			oddsum =oddsum + count

	return oddsum

get_odd(lists)

	



		



	





