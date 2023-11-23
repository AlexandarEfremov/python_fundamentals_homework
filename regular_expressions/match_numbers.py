import re

string_input = input()

pattern = r"(^|(?<=\s))-?\b(?:0|[1-9]\d*)(?:\.\d+)?\b($|(?=\s))"

matches = re.finditer(pattern, string_input)
for match in matches:
    print(match.group(), end=" ")
