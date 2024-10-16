userinput = "come go is ji come"

def get_duplicate(words):

	occur = 0

	for index in range(len(words)):
		occur = 1

		for elements in range(index):
			if words[index] == words[elements]:
				occur += 1

		if occur > 1:
			print(words[index])



get_duplicate(userinput)