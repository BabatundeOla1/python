sum = 0

for count in range(1, 11):

	score = int(input("Enter 10 Scores: "))
	sum += score

	if score < 0:
		break
		
print(f"Sum of all scores between 0 and 100=", sum)