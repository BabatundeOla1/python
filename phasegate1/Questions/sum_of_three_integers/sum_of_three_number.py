userinput = int(input("Enter number between 0 to 1000: "))

first_number = userinput // 100

second_number = (userinput // 10) % 10

third_number = userinput % 10 

sum = first_number + second_number + third_number

print(sum)



