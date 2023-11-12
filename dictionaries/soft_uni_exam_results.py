exam_dict = {}
exam_submissions = {}

while True:
    input_info = input()
    if input_info == "exam finished":
        break
    if "banned" in input_info:
        banned_user = input_info.split("-")[0]
        if banned_user in exam_dict.keys():
            del exam_dict[banned_user]
            continue
    username, language, points = input_info.split("-")
    points = int(points)

    if username not in exam_dict:
        exam_dict[username] = {'language': language, 'points': points}
    else:
        if exam_dict[username]['points'] < points:
            exam_dict[username]['points'] = points

    if language not in exam_submissions:
        exam_submissions[language] = 1
    else:
        exam_submissions[language] += 1

print("Results:")
for student, data in exam_dict.items():
    print(f"{student} | {data['points']}")
print("Submissions:")
for lang, submissions in exam_submissions.items():
    print(f"{lang} - {submissions}")
