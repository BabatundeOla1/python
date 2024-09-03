firstinput = int(input("Enter first input: "))

secondinput = int(input("Enter second input: "))

thirdinput = int(input("Enter third input: "))


def getmaximum(firstinput, secondinput, thirdinput):
	largest = 0

	if firstinput > largest: 
		largest = firstinput
		

	if secondinput > largest:
		largest = secondinput

	if thirdinput > largest:
		largest = thirdinput
	
	return largest

print(getmaximum(firstinput, secondinput, thirdinput))








