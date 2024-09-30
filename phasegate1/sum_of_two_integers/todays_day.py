userinput = int(input("Enter a number for today's day of the week: "))

userinput2 = int(input("Enter a number of days after today's for a future day: "))

0 = Sunday
1 = Monday
2 = Tuesday

if(userinput == 0 and userinput2 == 0):
	print(Sunday)

if(userinput == 1 and userinput2 == 1):
	print(Monday)

if(userinput == 2 and userinput2 == 2):
	print(Tuesday)

print("Today's is", userinput, "and the future day is", userinput2)