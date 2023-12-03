import re

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    password = input()
    pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]+)<\1"
    match = re.search(pattern, password)
    if not match:
        print("Try another password!")
    else:
        numbers = match.group(2)
        lower = match.group(3)
        upper = match.group(4)
        symbols = match.group(5)
        new_password = numbers + lower + upper + symbols
        print(f"Password: {new_password}")

