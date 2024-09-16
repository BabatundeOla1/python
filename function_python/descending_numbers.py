def descending_numbers(firstnumber, secondnumber, thirdnumber):

	highestnum = firstnumber
	secondhighest = firstnumber
	smallestnum = firstnumber
	sum = 0

	if firstnumber > secondnumber and firstnumber > thirdnumber:
		highestnum = firstnumber

	if secondnumber > firstnumber and secondnumber > thirdnumber:
		highestnum = secondnumber
	
	if thirdnumber > firstnumber and thirdnumber > secondnumber:
		highestnum = thirdnumber


	if firstnumber < secondnumber and firstnumber < thirdnumber:
		smallestnum = firstnumber

	if secondnumber < firstnumber and secondnumber < thirdnumber:
		smallestnum = secondnumber

	if thirdnumber < firstnumber and thirdnumber < secondnumber:
		smallestnum = thirdnumber

	sum = firstnumber + secondnumber + thirdnumber

	secondhighest = sum - highestnum - smallestnum

	print(highestnum, secondhighest, smallestnum)
	

descending_numbers(-7, -67, 90)