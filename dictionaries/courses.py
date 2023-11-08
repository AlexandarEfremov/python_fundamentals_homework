# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users. For each
# course, print the registered users.

courses_dict = {}

while True:
    input_command = input()
    if input_command == "end":
        break
    course_name, student_names = input_command.split(" : ")
    if course_name not in courses_dict.keys():
        courses_dict[course_name] = []

    courses_dict[course_name].append(student_names)

for course_name, students in courses_dict.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")
