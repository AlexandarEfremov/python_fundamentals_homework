import re
total_points = 0
input_string = input()
destination_list = []
pattern = r"=([A-Z][A-Za-z]{2,})=|\/([A-Z][A-Za-z]{2,})\/"
matches = re.finditer(pattern, input_string)
for match in matches:
    if match.group(1) is not None:
        variable_value = match.group(1)
        variable_len = len(variable_value)
        total_points += variable_len
        destination_list.append(variable_value)
    elif match.group(2) is not None:
        variable_value = match.group(2)
        variable_len = len(variable_value)
        total_points += variable_len
        destination_list.append(variable_value)

print(f"Destinations: {', '.join(destination_list)}")
print(f"Travel Points: {total_points}")

