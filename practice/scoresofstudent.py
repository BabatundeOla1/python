"""
initialize score to zero
initialize count to  zero
initialize average to zero

"""
total_score = 0

grade = 0

count = 0

while grade != -1:

	scores = int(input("Enter score of students: "))
	
	count = count + 1

	total_score = total_score + scores

	grade = int(input("Enter 0 to continue or (-1 to quit): "))

average = total_score / count 
print(average)
