firstinput = int(input("Enter first input: "))

secondinput = int(input("Enter second input: "))

thirdinput = int(input("Enter third input: "))


def getsmallest(firstinput, secondinput, thirdinput):
	smallest = 0

	if firstinput < smallest: 
		smallest = firstinput
		

	if secondinput < smallest:
		smallest = secondinput

	if thirdinput < smallest:
		smallest = thirdinput
	
	return smallest

print(getsmallest(firstinput, secondinput, thirdinput))