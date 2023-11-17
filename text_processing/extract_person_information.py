# Write a program that reads N lines of strings and extracts the name and the age of a given person:
#  The person's name will be surrounded by "@" and "|" in the format "@{name}|".
#  The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."


number_of_lines = int(input())


def name_check(string):
    name = ""
    for index, letter in enumerate(string):
        if letter == "@":
            rest_string = string[index + 1:]
            for i in rest_string:
                if i == "|":
                    break
                name += i
    return name


def age_check(string):
    age = ""
    for index, letter in enumerate(string):
        if letter == "#":
            rest_string = string[index + 1:]
            for i in rest_string:
                if i == "*":
                    break
                age += i
    return age


for _ in range(number_of_lines):
    str_input = input()
    given_name = name_check(str_input)
    given_age = age_check(str_input)
    print(f"{given_name} is {int(given_age)} years old.")





