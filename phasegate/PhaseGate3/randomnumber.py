import random

count = 0

count2 = 0

for subtraction in range(10):	

	random_number = random.randrange(10)

	random_number2 = random.randrange(10)

	if random_number > random_number2:
		
		temp = random_number

		random_number = random_number2

		random_number2 = temp

	print(random_number2, "-", random_number)

	userinput = int(input("Answer the above question: "))

	random_number_subtraction = random_number2 - random_number

	if(userinput == random_number_subtraction):
		count += 1
		print("correct answer")


	if(userinput != random_number_subtraction):
		count2 += 1

		print("Incorrect answer")



print("Total correct answer =", count)

print("Total incorrect answer =", count2)


