random = ['2','13', '14']

userinput = input("Guess the three Numbers: ")

count = userinput.split()

#print(count)

if(count[0] == random[0] and count[1] == random[1] and count[2] == random[2]):

	print("You win $5000")

elif count[0] != random[0] and count[1] == random[1] and count[2] == random[2]:

	print("You win $4000")

elif count[0] == random[0] and count[1] != random[1] and count[2] == random[2]:

	print("You win $3000")

elif count[0] == random[0] and count[1] == random[1] and count[2] != random[2]:

	print("You win $2000")

else:
	print("Tete No be your way BASTARD!!")
