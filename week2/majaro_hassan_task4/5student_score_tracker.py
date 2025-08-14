'''5. Student Score Tracker
'''
name_list = []
score_list = []
student_names = input("Input 3 student names separated by space: ")
new_student_names = student_names.split()
student1 = input(f"Input {new_student_names[0]} score: ")
student2 = input(f"Input {new_student_names[1]} score: ")
student3 = input(f"Input {new_student_names[2]} score: ")
student_score_list = [student1, student2, student3]

print("Student Score Table")
print(f"{new_student_names[0]}\t- {student_score_list[0]}")
print(f"{new_student_names[1]}\t- {student_score_list[1]}")
print(f"{new_student_names[2]}\t- {student_score_list[2]}")