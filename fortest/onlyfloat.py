def only_float(price, discount):

	if price < 0 and discount < 0:
		raise ValueError("Input can not be negative!")
	
	PERCENTAGE = 100

	discount_in_percentage = discount / PERCENTAGE

	the_price = price * discount_in_percentage

	discount_price = price - the_price

	return discount_price