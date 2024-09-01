"""prompt uder to enter input between 1 and 10
store number as userinput
count the number of column 
use for loop to count the number 
display result

"""




userinput = int(input("Enter a number between 1 and 10: \n"))


for column in range(1, 11):

	print(f"{userinput} x {column} = {userinput * column}")
	 




    