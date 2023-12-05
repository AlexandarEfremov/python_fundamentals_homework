import re

input_string = input()
pattern = r"=([A-Z][A-Za-z]{2,})=|\/([A-Z][A-Za-z]{2,})\/"
results = re.findall(pattern, input_string)
print(results)
total_points = [len(match) for match in results]
print(total_points)