user1 = int(input("Enter integer 1: "))
user2 = int(input("Enter integer 2: "))
user3 = int(input("Enter integer 3: "))

largest = user1
smallest = user1
sum = 0

if user1 > user2 and user1 > user3:
	largest = user1

if user2 > user1 and user2 > user3:
	largest = user2

if user3 > user1 and user3 > user2:
	largest = user3


if user1 < user2 and user1 < user3:
	smallest = user1

if user2 < user1 and user2 < user3:
	smallest = user2

if user3 < user1 and user3 < user2:
	smallest = user3

sum = user1 + user2 + user3

secondlargest = sum - largest - smallest

print(smallest,"\n",secondlargest,"\n",largest)

