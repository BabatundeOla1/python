userinput = int(input("Enter a number: "))

def get_factorial(number):
	
	factorial = 1
	for count in range(number, 0, -1):

		factorial = factorial * count

	return factorial

		
print(get_factorial(userinput))
	

	
	
	