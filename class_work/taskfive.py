sum = 0

sum_of_even_scores = 0
for count in range(1, 11):

	score = int(input("Enter 10 Scores: "))

	if score % 2 == 0:
		sum_of_even_scores += score

print(f"sum of all even scores =", sum_of_even_scores)