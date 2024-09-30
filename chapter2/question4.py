passes = 0
failures = 0

for studet in range(10):
	result = int(input("input the next result: "))

	if (result > 1):
		passes+=1
	else:
		failures+=1
print("Total number of student that failed:",failures)
print("Total number of student that passed:", passes)



for count in range(2):
	userinput = int(input("Enter 2 integers: "))

	if (userinput % 2 == 0):
		print("it is Even")

	else:
		print("it is odd")
