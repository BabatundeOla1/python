for numbers in range(1000, 3000):

	firstnumber = numbers // 1000

	secondnumber = numbers // 100 % 10

	thirdnumber= numbers // 10 % 10

	fourthnumber = numbers % 10

	if(firstnumber % 2 == 0 and secondnumber % 2 == 0 and thirdnumber % 2 == 0 and fourthnumber % 2 == 0):

		print(numbers, end=", ")
