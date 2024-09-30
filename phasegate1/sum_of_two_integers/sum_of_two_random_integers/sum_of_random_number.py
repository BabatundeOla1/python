import random

random_number = random.randrange(10, 100)
print(random_number)

userinput = int(input("Enter the sum of the random number generated: "))

first_radom_number = random_number // 10

second_random_number = random_number % 10

sum = first_radom_number + second_random_number

if(userinput == sum):

	print("true")
else:
	print("false")