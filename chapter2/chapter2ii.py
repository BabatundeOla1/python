user1 = int(input("Enter integer 1: "))
user2 = int(input("Enter integer 2: "))
user3 = int(input("Enter integer 3: "))

largest = user1
smallest = user1
sum = 0
average = 0 
product = 1


sum = user1 + user2 + user3

average = sum / 3

product = user1 * user2 * user3


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


print("Largest = ",largest)
print("Smallest = ",smallest)
print("Sum is= ",sum)
print("average is= ",average)
print("Product is= ",product)
