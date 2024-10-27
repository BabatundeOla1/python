userinput = input("Enter card number: ")

if not userinput.isdigit():
	raise ValueError("input must be only digit")

def validate_card(input):

	try:
		if not isinstance(input, str):
			raise TypeError("Input must be a string.")

		if not input.isdigit():
			raise ValueError("input must be only digit")

		if input.startswith("4"):
			return "VisaCard"

		elif input.startswith("5"):
			return "MasterCard"

		elif input.startswith("6"):
			return "Discover Credit Card"

		elif input.startswith("37"):
			return "America Express"

		else:
			return "Invalid Card"

	except TypeError as e:
		return f"Error: {e}"

	except ValueError as e:
		return f"Error: {e}"
		

def check_validity(input):

	try:
		if not isinstance(input, str):
			raise TypeError("Input must be a string.")

		if not input.isdigit():
			raise ValueError("input must be only digit")
	
		sum_odd = sum_even = total_sum = 0

		size = len(input)

		for index in range(size):
		
			if(size - index) % 2 == 0:

				doubled_integer = int(input[index]) * 2	
					
				if doubled_integer > 9:
			
					doubled_integer = (doubled_integer // 10) + (doubled_integer % 10)
				
				sum_even += doubled_integer
			
			else:			
				sum_odd += int(input[index])

			total_sum = sum_even + sum_odd

		if total_sum % 10 == 0:
			return "Valid"

		else:
			return "Invalid"

	except TypeError as e:
		return f"Error: {e}"

	except ValueError as e:
		return f"Error: {e}"
		

print("************************************")

print("Credit Card Number:", userinput)
print("Credit Card Type:", validate_card(userinput))
print("Credit Card Digit Length:", len(userinput))
print("Card Type:", check_validity(userinput))

print("************************************")



