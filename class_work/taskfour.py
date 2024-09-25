sum = 0

counter = 0
for count in range(1, 11):

	score = int(input("Enter 10 Scores: "))

	if count % 2 == 0:
		counter += count

print(f"sum of all even indexes =", counter)