# Write a program that reads a string from the console and replaces any sequence of the same letters with a single
# corresponding letter

input_string = input()

last_string = ''
new_string = ''

for letter in input_string:
    if letter != last_string:
        new_string += letter
        last_string = letter
print(new_string)
