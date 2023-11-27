participant_names = {name: 0 for name in input().split(", ")}
import re
name_pattern = r"([A-Za-z]+)"
distance_pattern = r"(\d)"

while True:
    input_info = input()
    if input_info == "end of race":
        break
    match_name = ""
    for match in re.finditer(name_pattern, input_info):
        match_name += match.group()

    match_distance = 0
    for match in re.finditer(distance_pattern, input_info):
        match_distance += int(match.group())

    if match_name in participant_names:
        participant_names[match_name] += match_distance
    else:
        continue


sorted_participants = dict(sorted(participant_names.items(), key=lambda item: item[1], reverse=True))
counter = 0
for key, value in sorted_participants.items():
    if counter == 3:
        break
    if counter == 0:
        print(f"1st place: {key}")
    elif counter == 1:
        print(f"2nd place: {key}")
    elif counter == 2:
        print(f"3rd place: {key}")
    counter += 1