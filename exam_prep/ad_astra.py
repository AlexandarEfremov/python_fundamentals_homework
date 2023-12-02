import re

text_string = input()
pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, text_string)
total_calories = [sum([int(match[3]) for match in matches])]
valid_items = [f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}" for match in matches]

print(f"You have food to last you for: {total_calories[0] // 2000} days!")
for i in valid_items:
    print(i)
