name = input("What is your name? ")

def personality_questions_extrovert_introvert(name):
	extrovert_and_introvert = [["A: Expend energy, enjoy groups", "B: conservative energy, enjoy one on one", " "],
				["A: more outgoing, thinking loud", "B: more reserved, thinking to yourself", " "],
				["A: seek many tasks, public activities, interaction with others", "B: seek private, solitary activities with quiet to concentrate", " "],
				["A: external, communicative, express yourself", "B: internal, reticient, keep to yourself", " "],
				["A: active, initiate", "B: reflective, delibrate", " "]]
	
	total_answer_a = 0
	total_answer_b = 0

	for index in range(len(extrovert_and_introvert)):
	
		while True:
			print(f"Question {index + 1}: ")
			print(extrovert_and_introvert[index][0], extrovert_and_introvert[index][1])

			user_input = input().upper()

			if user_input == "A":
				extrovert_and_introvert[index][2] = "A"
				total_answer_a += 1
				break
			elif user_input == "B":
				extrovert_and_introvert[index][2] = "B"
				total_answer_b += 1
				break
			else:
				print("Expected A or B as response\n I know this is an error please try again")
	print()
	print(f"Hello {name} You Selected:")

	for answer in range(len(extrovert_and_introvert)):
		if extrovert_and_introvert[answer][2] == "A":
			print(extrovert_and_introvert[answer][0])
		if extrovert_and_introvert[answer][2] == "B":
			print(extrovert_and_introvert[answer][1])
	print()
	print(f"Number of A selected: {total_answer_a}")
	print(f"Number of B selected: {total_answer_b}")
	if total_answer_a > 2:
		print("E")
	else:
		print("I")
print(personality_questions_extrovert_introvert(name))


def personality_questions_sensing_and_intuitive(name):
	sensing_and_intuitive = [["A: Interpret literally", "B: look for meaning and possibilities", " "],
				["A: practical, realistic, experimental", "B: imaginative, innovative, theoretical", " "],
				["A: Standard, usual, conventional", "B: different, novel, unique", " "],
				["A: focus on here and now", "B: look to the future, global perspective, big picture", " "],
				["A: facts, things, what is", "B: ideas, dreams, what could be, philosophical", " "]]

	total_answer_a = 0
	total_answer_b = 0

	for index in range(len(sensing_and_intuitive)):

		while True:

			print(f"Question {index + 1}: ")
			print(sensing_and_intuitive[index][0], sensing_and_intuitive[index][1])
	
			user_input = input().upper()

			if user_input == "A":
				sensing_and_intuitive[index][2] = "A"
				total_answer_a += 1
				break

			elif user_input == "B":
				sensing_and_intuitive[index][2] = "B"
				total_answer_b += 1
				break
		
			else:
				print("Expected A or B as response\n I know this is an error please try again")
				

	print()
	print(f"Hello {name} You Selected:")

	for answer in range(len(sensing_and_intuitive)):
		
		if sensing_and_intuitive[answer][2] == "A":
			print(sensing_and_intuitive[answer][0])

		if sensing_and_intuitive[answer][2] == "B":
			print(sensing_and_intuitive[answer][1])

	print()
	print(f"Number of A selected: {total_answer_a}")
	print(f"Number of B selected: {total_answer_b}")

	if total_answer_a > 2:
		print("S")
	else:
		print("N")

print(personality_questions_sensing_and_intuitive(name))



def personality_questions_thinking_and_feeling(name):
	thinking_and_feeling = [["A: logical, thinking, questioning", "B: empathetic, feeling, accommodating", " "],
				["A: candid, straight forward, frank", "B: tactful, kind, encouraging", " "],
				["A: firm, tend to criticize, hold the line", "B: gentle, tend to appreciate, conciliate", " "],
				["A: tough-minded, just", "B: tender-hearted, merciful", " "],
				["A: matter of fact, issue-oriented", "B: senstive, people-oriented, compassionate", " "]]


	total_answer_a = 0
	total_answer_b = 0

	for index in range(len(thinking_and_feeling)):
	
		while True:

			print(f"Question {index + 1}: ")
			print(thinking_and_feeling[index][0], thinking_and_feeling[index][1])

			user_input = input().upper()

			if user_input == "A":
				thinking_and_feeling[index][2] = "A"
				total_answer_a += 1
				break

			elif user_input == "B":
				thinking_and_feeling[index][2] = "B"
				total_answer_b += 1
				break

			else:
				print("Expected A or B as response\n I know this is an error please try again")
				

	print()
	print(f"Hello {name} You Selected:")

	for answer in range(len(thinking_and_feeling)):

		if thinking_and_feeling[answer][2] == "A":
			print(thinking_and_feeling[answer][0])

		if thinking_and_feeling[answer][2] == "B":
			print(thinking_and_feeling[answer][1])

	print()
	print(f"Number of A selected: {total_answer_a}")
	print(f"Number of B selected: {total_answer_b}")

	if total_answer_a > 2:
		print("T")
	else:
		print("F")


print(personality_questions_thinking_and_feeling(name))



def personality_questions_judging_and_perceptive(name):
	judging_and_perceptive = [["A: organized, orderly", "B: flexible, adaptable", " "],
				["A: candid, straight forward, frank", "B: tactful, kind, encouraging", " "],
				["A: firm, tend to criticize, hold the line", "B: gentle, tend to appreciate, conciliate", " "],
				["A: tough-minded, just", "B: tender-hearted, merciful", " "],
				["A: matter of fact, issue-oriented", "B: sensitive, people-oriented, compassionate", " "]]

	total_answer_a = 0
	total_answer_b = 0

	for index in range(len(judging_and_perceptive)):

		while True:
			print(f"Question {index + 1}: ")
			print(judging_and_perceptive[index][0], judging_and_perceptive[index][1])

			user_input = input().upper()

			if user_input == "A":
				judging_and_perceptive[index][2] = "A"
				total_answer_a += 1
				break
            
			elif user_input == "B":
                
				judging_and_perceptive[index][2] = "B"
				total_answer_b += 1
				break
           
			else:
				print("Expected A or B as response\n I know this is an error please try again")

	print()
	print(f"Hello {name} You Selected:")

	for answer in range(len(judging_and_perceptive)):

		if judging_and_perceptive[answer][2] == "A":
			print(judging_and_perceptive[answer][0])
       
		if judging_and_perceptive[answer][2] == "B":
			print(judging_and_perceptive[answer][1])

   
	print()
	print(f"Number of A selected: {total_answer_a}")
	print(f"Number of B selected: {total_answer_b}")

	if total_answer_a > 2:
		print("J")

	else:
		print("P")

print(personality_questions_judging_and_perceptive(name))




