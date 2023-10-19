lessons_input = input().split(", ")
lessons_list = lessons_input.copy()
while True:
    input_command = input().split(":")
    if input_command[0] == "course start":
        break
    if input_command[0] == "Add":
        lesson_name = input_command[1]
        if lesson_name not in lessons_list:
            lessons_list.append(lesson_name)
    elif input_command[0] == "Insert":
        lesson_name = input_command[1]
        lesson_index = int(input_command[2])
        if 0 <= lesson_index < len(lessons_list):
            if lesson_name not in lessons_list:
                lessons_list.insert(lesson_index, lesson_name)
    elif input_command[0] == "Remove":
        lesson_name = input_command[1]
        if lesson_name in lessons_list:
            lessons_list.remove(lesson_name)
            if f"{lesson_name}-Exercise" in lessons_list:
                lessons_list.remove(f"{lesson_name}-Exercise")
    elif input_command[0] == "Swap":
        lesson_title_one = input_command[1]
        lesson_title_two = input_command[2]
        if lesson_title_one in lessons_list and lesson_title_two in lessons_list:
            index_one = lessons_list.index(lesson_title_one)
            index_two = lessons_list.index(lesson_title_two)
            lessons_list[index_one], lessons_list[index_two] = lessons_list[index_two], lessons_list[index_one]
            if f"{lesson_title_one}-Exercise" in lessons_list:
                index_exercise = lessons_list.index(f"{lesson_title_one}-Exercise")
                popped_exercise = lessons_list.pop(index_exercise)
                lessons_list.insert(index_two + 1, popped_exercise)
            elif f"{lesson_title_two}-Exercise" in lessons_list:
                index_exercise = lessons_list.index(f"{lesson_title_two}-Exercise")
                popped_exercise = lessons_list.pop(index_exercise)
                lessons_list.insert(index_one + 1, popped_exercise)
    elif input_command[0] == "Exercise":
        lesson_title = input_command[1]
        if lesson_title in lessons_list:
            lesson_title_index = lessons_list.index(lesson_title)
            lessons_list.insert(lesson_title_index + 1, f"{lesson_title}-Exercise")
        else:
            lessons_list.append(lesson_title)
            ex = f"{lesson_title}-Exercise"
            lessons_list.append(ex)

indexed_titles = [(index + 1, title) for index, title in enumerate(lessons_list)]
for index, title in indexed_titles:
    print(f"{index}.{title}")

# Data Types, Objects, Lists
