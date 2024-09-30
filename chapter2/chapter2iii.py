userinput = int(input("Enter five integers: "))

firstnumber = userinput // 10000

secondnumber =  (userinput // 1000) % 10

thirdnumber = (userinput // 100) % 10
32
fourthnumber = (userinput // 10) % 10

fifthnumber = userinput % 10

print(firstnumber, "", secondnumber, "", thirdnumber, "", fourthnumber, "", fifthnumber)