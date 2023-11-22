contest_pass_dict = {}
secondary_dict = {}

# Input for contests and passwords
while True:
    info_input = input()
    if "end of contests" in info_input:
        break
    contest, password = info_input.split(":")
    contest_pass_dict[contest] = password

while True:
    second_input = input()
    if "end of submissions" in second_input:
        break
    contest_check, password_check, username, points = second_input.split("=>")

    # Check if the contest exists and the password is correct
    if contest_check not in contest_pass_dict or password_check != contest_pass_dict[contest_check]:
        continue

    if username not in secondary_dict:
        secondary_dict[username] = {contest_check: int(points)}
    elif contest_check not in secondary_dict[username]:
        secondary_dict[username][contest_check] = int(points)
    elif contest_check in secondary_dict[username]:
        if int(points) > secondary_dict[username][contest_check]:
            secondary_dict[username][contest_check] = int(points)

# Calculate total points for each candidate
candidate_results = {}
for candidate, results in secondary_dict.items():
    candidate_results[candidate] = sum(results.values())

# Find the best candidate
best_candidate = max(candidate_results, key=candidate_results.get)

# Display the result
print(f"Best candidate is {best_candidate} with total {candidate_results[best_candidate]} points.")
print("Ranking:")
for student in sorted(secondary_dict.keys()):
    print(student)
    for contest, points in sorted(secondary_dict[student].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {points}")

