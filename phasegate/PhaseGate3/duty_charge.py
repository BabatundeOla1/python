userinput = int(input("Enter the cost of a car: "))

PERCENTAGE = 100

duty_charge = 0

if(userinput <= 0):
	print("Invalid Amount")

if(userinput >= 10000000):
	duty_charge = userinput * 20 / PERCENTAGE

elif(userinput >= 5000000 and userinput < 10000000):
	duty_charge = userinput * 15 / PERCENTAGE

elif(userinput >= 2500000 and userinput < 5000000):
	duty_charge = userinput * 10 / PERCENTAGE

elif(userinput < 2500000):
	duty_charge = userinput * 5 / PERCENTAGE

print(duty_charge)

