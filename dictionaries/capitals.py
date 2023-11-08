# Using a dictionary comprehension, write a program that receives country names on the first line, separated by
# comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and
# space ", "). Print each country with their capital on a separate line in the following format: "{country} ->
# {capital}".

input_line_one = input().split(", ")
input_line_two = input().split(", ")

result = zip(input_line_one, input_line_two)
country_dict = {country: capital for country, capital in result}

for country, capital in country_dict.items():
    print(f"{country} -> {capital}")

