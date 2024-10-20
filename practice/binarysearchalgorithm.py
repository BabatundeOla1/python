list = [15, 7, 3, 98, 35, 16]
item = 16

def get_number(arr, lucky_number):

	low = 0
	high = len(list)-1

	while low <= high:
		mid_number = low + high
		guess = mid_number

		if guess == lucky_number:
			return mid_number

		if guess > lucky_number:
			high = mid -1

		else:
			



print(get_number(list, item))