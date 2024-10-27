def personality_questions_extrovert_introvert(name):
    extrovert_and_introvert = [
        ["A: Expend energy, enjoy groups", "B: conservative energy, enjoy one on one", " "],
        ["A: more outgoing, thinking loud", "B: more reserved, thinking to yourself", " "],
        ["A: seek many tasks, public activities, interaction with others", "B: seek private, solitary activities with quiet to concentrate", " "],
        ["A: external, communicative, express yourself", "B: internal, reticient, keep to yourself", " "],
        ["A: active, initiate", "B: reflective, delibrate", " "]
    ]

    total_answer_a = 0
    total_answer_b = 0

    for index in range(len(extrovert_and_introvert)):
        print(f"Question {index + 1}: ")
        print(extrovert_and_introvert[index][0], extrovert_and_introvert[index][1])

        user_input = input().upper()

        if user_input == "A":
            extrovert_and_introvert[index][2] = "A"
            total_answer_a += 1
        elif user_input == "B":
            extrovert_and_introvert[index][2] = "B"
            total_answer_b += 1
        else:
            print("Expected A or B as response\n I know this is an error please try again")
            index -= 1

   