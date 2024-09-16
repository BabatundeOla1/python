user_input = int(input("Enter year: "))

def leap_year(year):

	if year % 4 == 0 and year % 100 != 0:

		print("It is a Leap year.")
 
	else:

		print("It is not a Leap year.")

	