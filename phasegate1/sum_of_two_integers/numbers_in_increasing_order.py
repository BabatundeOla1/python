first_number  = int(input("Enter first integer: "))

second_number  = int(input("Enter second integer: "))

third_number  = int(input("Enter third integer: "))

largest_number = first_number

smallest_number = first_number

if(first_number > second_number and first_number > third_number):
	largest_number = first_number

if(second_number > first_number and second_number > third_number):
	largest_number = second_number

if(third_number > first_number and third_number > second_number):
	largest_number = third_number


if(first_number < second_number and first_number < third_number):
	smallest_number = first_number

if(second_number < first_number and second_number < third_number):
	smallest_number = second_number

if(third_number < first_number and third_number < second_number):
	smallest_number = third_number

sum = first_number + second_number + third_number

middle_number = sum - largest_number - smallest_number

print(smallest_number, middle_number, largest_number)

