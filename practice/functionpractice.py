'''
def greet(number, score):

	multi = number * 5
	return multi + score 
	
	 

add = greet(5, 6)

print(add)

#using star args
def add_all(*number):

	return sum(number)
	

print(add_all(4, 16, 25, 36, 81))


#using star kwags
def using_star_kwargs(**words):

	for key, value in words.items():
		print(f"{key}: {value}")

using_star_kwargs(name="john", greeting="Hello")
'''

def is_prime(number):

	if number % 2 != 0 and number % 3 != 0:
		return True

	else:
		return False

prime = is_prime(113)
print(prime)