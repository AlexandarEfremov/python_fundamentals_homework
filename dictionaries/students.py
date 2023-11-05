# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique

students = []
course_to_check = None

while True:
    student_info = input()

    if ":" not in student_info:
        course_to_check = student_info
        break
    name, ID, course = student_info.split(":")
    students.append({"name": name, "ID": ID, "course": course})


for student in students:
    if course_to_check.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")
