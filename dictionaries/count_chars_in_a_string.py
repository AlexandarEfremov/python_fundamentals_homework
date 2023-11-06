# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

input_text = input().replace(" ", "")
input_dict = {}

for letter in input_text:
    if letter not in input_dict:
        input_dict[letter] = 1
    else:
        input_dict[letter] += 1

for key, value in input_dict.items():
    print(f"{key} -> {value}")