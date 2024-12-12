import random
import math

for roll in range(10):
    print(random.randint(1, 7), end=" ")

# for coin in range(20):
#     print("Head" if random.randrange(2) == 0 else "Tail")
#
#
# #
# frequency1 = 0
# frequency2 = 0
# frequency3 = 0
# frequency4 = 0
# frequency5 = 0
# frequency6 = 0
#
# for roll in range(6_000_000):
#     face = random.randrange(6)
#
#     if face == 1:
#         frequency1 += 1
#     elif face == 2:
#         frequency2 += 1
#     elif face == 3:
#         frequency3 += 1
#     elif face == 4:
#         frequency4 += 1
#     elif face == 5:
#         frequency5 += 1
#     elif face == 6:
#         frequency6 += 1
#
# print(f'Face{"Frequency":>13}')
# print(f'{1:>4}{frequency1:>13}')
# print(f'{2:>4}{frequency2:>13}')
# print(f'{3:>4}{frequency3:>13}')
# print(f'{4:>4}{frequency4:>13}')
# print(f'{5:>4}{frequency5:>13}')
# print(f'{6:>4}{frequency6:>10}')

student = ('sue [23, 34, 45]')
print(student)

def rectangle_area(length=3, width=2):
    return length * width

print(rectangle_area(7, 10))

def get_average(*args):
    return sum(args) / len(args)

print(get_average(2,3,4))
def calculate_product(*args):
    product = 1
    for values in args:
        product *= values
    return product

print(calculate_product(10,20,30))
print(calculate_product(*range(1,6,)))