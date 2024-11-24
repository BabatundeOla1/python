numbers = list(range(1,16))
print(numbers)

duplicate_of_numbers = numbers * 2
print(duplicate_of_numbers)

remove_number = list(set(duplicate_of_numbers))
print(remove_number)

def add_every_third_number(numbers):
    for elements in range(2, len(numbers), 3):
        numbers[elements] += numbers[elements]
    print(numbers[elements])

add_every_third_number(numbers)

