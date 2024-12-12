word = "CODEDAMN"
number = 2

def encrypt(word, number):
    _validate_number(number)
    new_words = ""
    for text in word:
        if text.isupper():
            new_words += chr(ord(text) + number)
        elif text.islower():
            new_words += chr(ord(text) + number)
    return new_words

def decrypt(word, number):
    _validate_number(number)
    new_words = ""
    for text in word:
        if text.isupper():
            new_words += chr(ord(text) - number)
        elif text.islower():
            new_words += chr(ord(text) - number)
    return new_words

def _validate_number(number):
    if number < 0:
        raise ValueError("Number must be Greater than 1")
    return number