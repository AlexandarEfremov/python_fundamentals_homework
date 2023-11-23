import re


pattern = r"\d+"
string_input = input()
while string_input:
    result = re.findall(pattern, string_input)
    if result:
        print(" ".join(result), end=" ")
    string_input = input()


