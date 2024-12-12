responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 14]
frequency = []
for score in responses:
    for element in responses:
        if element == element + 1:
            frequency[element] += 1
            print(frequency[element])