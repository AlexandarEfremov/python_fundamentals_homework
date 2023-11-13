# You will be given strings on separate lines until you receive an "end" command. Write a program that reverses
# strings and prints each pair on a separate line in the format "{word} = {reversed_word}"

string_dict = {}

while True:
    string_input = input()
    if string_input == "end":
        break
    reversed_string = string_input[::-1]
    string_dict[string_input] = reversed_string

for key, value in string_dict.items():
    print(f"{key} = {value}")

