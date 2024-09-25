sum = 0

average = 0

for count in range(1, 11):

	score = int(input("Enter 10 Scores: "))

	sum = sum + score

average = sum / count

print(average)