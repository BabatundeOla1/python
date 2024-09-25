def get_evennumber(number):

		if number > 999 and number < 0:
			print("Invalid")

		if number % 2 == 0:
			
			total_number = 0

			firstnumber = number // 100
			secondnumber = number // 10 % 10
			thirdnumber = number % 10
			
			total_number = firstnumber + secondnumber + thirdnumber

		return total_number

print(get_evennumber(888))