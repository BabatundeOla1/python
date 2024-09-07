userinput = int(input("Enter two numbers: "))

firstnumber = userinput / 10

secondnumber = userinput % 10;

if firstnumber == secondnumber:
	print(0)
	
if firstnumber > secondnumber:
	print(1)
	
if firstnumber < secondnumber:
	print(-1)