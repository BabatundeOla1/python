userinput = int(input("Enter the number of columns: "))

for rows in range(userinput):
    for columns in range(rows):
        print("*", end=" ")
    print()