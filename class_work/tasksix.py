average = 0
sum_of_even = 0
counter = 0

for count in range(1, 11):

	score = int(input("Enter 10 Scores: "))

	if score % 2 == 0:
		sum_of_even += score
		
		counter+=1

	average = sum_of_even / counter
	

print(f"average of all even scores =", average)