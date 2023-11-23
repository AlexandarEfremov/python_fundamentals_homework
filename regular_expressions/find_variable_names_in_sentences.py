import re
test_string = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern,test_string)

print(",".join(matches))