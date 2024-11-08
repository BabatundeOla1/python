
number_of_students = int(input("How many students do you have? "))
number_of_subjects = int(input("How many subjects do you offer?: "))

print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def get_student_scores_and_grade(number_of_students, number_of_subjects):

	student_grades = [[0] * number_of_students] * number_of_subjects

	for scores in range(1, number_of_students + 1):

		print(f"Entering Score for student {scores}.")

		for subjects in range(1, number_of_subjects + 1):	
	
			student_subject = int(input(f"Enter score for subject {subjects}: "))

			studentsGrades[students][subjects] = student_subjects

			if(student_subject < 0 or student_subject > 100):
				print("Invalid Input, Enter Score Again")
				#subjects--

userinput = get_student_scores_and_grade(number_of_students, number_of_subjects)
print(userinput)
	
	