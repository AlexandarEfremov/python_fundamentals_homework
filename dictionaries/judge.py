contest_dict = {}
individual_results = {}

while True:
    input_info = input()
    if input_info == "no more time":
        break
    username, contest, points = input_info.split(" -> ")
    points = int(points)

    if contest not in contest_dict:
        contest_dict[contest] = []

    if (username, points) not in contest_dict[contest]:
        contest_dict[contest].append((username, points))

    if username not in individual_results.keys():
        individual_results[username] = points
    else:
        individual_results[username] += points

for contest, participants in sorted(contest_dict.items()):
    print(f"{contest}: {len(participants)} participants")
    sorted_part = sorted(participants, key=lambda x: (-x[1], x[0]))
    for i, (participant, points) in enumerate(sorted_part, 1):
        print(f"{i}. {participant} <::> {points}")

print("Individual standings:")
sorted_participants = sorted(individual_results.items(), key=lambda x: (-x[1], x[0]))
for i, (username, points) in enumerate(sorted_participants, 1):
    print(f"{i}. {username} -> {points}")
