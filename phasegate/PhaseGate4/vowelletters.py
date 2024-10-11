userinput = input("Enter letter: ")

def get_vowel(words):

	for letters in range(len(words)):
		if (words[letters] == "a" or words[letters] == "e"  or words[letters] == "i"  or words[letters] == "o"  or words[letters] == "u"):
			return True

		else:
			return False

		
print(get_vowel(userinput))



