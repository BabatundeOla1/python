sum_of_multiple = 0

for numbers in range(0, 20_001):

	if numbers % 10 == 0:

		sum_of_multiple = sum_of_multiple + numbers

print(sum_of_multiple)