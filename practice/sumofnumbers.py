# value = [1,2,3,4,5,6,7,8]
#
# def getevennumbers(numbers):
#     for numb in numbers:
#         if(numb % 2 == 0):
#             print(numb)
#
# getevennumbers(value)
#
# 2 Extract the string in the list
given = [1,2,"a",3,9,"r", "5"]
# def extractstring(given):
#     out = " "
#     for numbers in given:
#         if isinstance(numbers, str):
#             out += numbers
#     print(out)
#
# extractstring(given)

# given1 = [1, 12, 9, 3, 2]
# # find any two numbers that gives the sum of 10
# point = 10
# def findnumber(given, point):
#     emptyarr = []
#     for numbers in given:
#         for count in numbers:
#             if numbers + count == point:
#                 emptyarr.append(numbers + count)
#                 return emptyarr
#
# print(findnumber(given1, point))


#3 check if a string is a palindrome
# words = "MADAM"
# def palindrom_check(letters):
#     new_words = ""
#     for alphabets in reversed(letters):
#         new_words += alphabets
#     if new_words == letters:
#         return True
#     else:
#         return False
#
# print(palindrom_check(words))

# # 4 Check for the Occurrencies in the list
# my_list = ["A","A","W","R","G","E","A"]
# def check_occurrence(my_list):
#     most_frequent = max(my_list, key=my_list.count)
#     return most_frequent
#
# print(check_occurrence(my_list))

#5 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
num = [2,7,11,15]
target = 9
def two_sum(nums, target):
    output = [ ]
    for index in range(len(nums)):
        for elemets in range(index+1, len(nums)):
            if nums[index] + nums[elemets] == target:
                output = index
                output = elemets
    return output

print(two_sum(num, target))