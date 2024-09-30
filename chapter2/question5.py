'''print("Number","\t","Square","","Cube")

for count in range(0, 6):
	number = count
	
	square = count**2

	cube = count**3

	
	print(number,"\t",square," \t",cube)
'''



print("Number","\t","Square","","Cube")

for count in range(0, 6):
	number = count
	
	square = count**2

	cube = count**3

	
	print("    ",number,"     ",square,"    ",cube)


for row in range(1, 6):

	for column in range(1, row+1):
		print("*",end = " ")

	print()


