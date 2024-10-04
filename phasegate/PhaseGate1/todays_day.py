userinput = int(input("Enter a number for today's day of the week: "))

userinput2 = int(input("Enter a number of days after today's for a future day: "))

if(userinput == 0):
	userinput = "Sunday"

if(userinput == 1):
	userinput = "Monday"

if(userinput == 2):
	userinput = "Tuesday"

if(userinput == 3):
	userinput = "Wednesday"

if(userinput == 4):
	userinput = "Thursday"

if(userinput == 5):
	userinput = "Friday"

if(userinput == 6):
	userinput = "Saturday"

if(userinput2 == 0):
	userinput2 = "Sunday"

if(userinput2 == 1):
	userinput2 = "Monday"

if(userinput2 == 2):
	userinput2 = "Tuesday"

if(userinput2 == 3):
	userinput2 = "Wednesday"

if(userinput2 == 4):
	userinput2 = "Thursday"

if(userinput2 == 5):
	userinput2 = "Friday"

if(userinput2 == 6):
	userinput2 = "Saturday"

print("Today's is", userinput, "and the future day is", userinput2)