userinput = int(input("Enter integer: "))

def reverse(number):

	reverse = 0

	while(number != 0):

		reverse = (reverse * 10) + number % 10

		number = number // 10

	return reverse

reverse(userinput)


def is_palindrome(number2):

	if(reverse(number2) == userinput):
		print("true")


	if(reverse(number2) != userinput):
		print("false")



is_palindrome(userinput)