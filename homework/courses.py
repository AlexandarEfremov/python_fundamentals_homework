# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
# You should create a list of courses and print it

single_n = int(input())
course = []
for _ in range(single_n):
    course_name = input()
    course.append(course_name)
print(course)