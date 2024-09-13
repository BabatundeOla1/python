"""x = 1
y = 2 

x, y = (y, x)

print(x, y)"""




def add_multiplication(*userInput):
	total = 1
	for userInput in userInput:
		total*=userInput

	return total

print(add_multiplication(3, 5, 3, 3, 3, 5))