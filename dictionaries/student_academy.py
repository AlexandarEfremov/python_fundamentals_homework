# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will
# be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to
# 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2
# nd decimal place
student_dict = {}
final_dict = {}
pair_of_rows = int(input())

for _ in range(pair_of_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in student_dict:
        student_dict[student_name] = student_grade
    else:
        new_grade = (student_dict[student_name] + student_grade) / 2
        student_dict[student_name] = new_grade

for key, value in student_dict.items():
    if value >= 4.5:
        final_dict[key] = value

for key, value in final_dict.items():
    print(f"{key} -> {value:.2f}")
