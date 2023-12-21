user_dict = {"user": {}, "contest": {}}
user_d = "user"
contest_d = "contest"


while True:
    command = input().split(" -> ")
    if command[0] == "no more time":
        break
    username, contest, points = command[0], command[1], int(command[2])

    if contest not in user_dict[contest_d]:
        user_dict[contest_d][contest] = {}

    if username not in user_dict[contest_d][contest]:
        user_dict[contest_d][contest][username] = 0

    if username not in user_dict[user_d]:
        user_dict[user_d][username] = 0

    if username in user_dict[user_d] and user_dict[user_d][username] == points:
        user_dict[user_d][username] += points

    if user_dict[contest_d][contest][username] < points:
        user_dict[user_d][username] += points - user_dict[contest_d][contest][username]
        user_dict[contest_d][contest][username] = points


sorted_stats = sorted(user_dict["user"].items(), key=lambda item: (-item[1], item[0]))

for key, value in user_dict[contest_d].items():
    len_of_users = len(value)
    print(f"{key}: {len_of_users} participants")
    for position, (name, points) in enumerate(
            sorted(user_dict[contest_d][key].items(), key=lambda item: (-item[1], item[0]))):
        print(f"{position}. {name} <::> {points}")

print("Individual standings:")
counter = 1
for participant, points in sorted_stats:
    print(f"{counter}. {participant} -> {points}")
    counter += 1





