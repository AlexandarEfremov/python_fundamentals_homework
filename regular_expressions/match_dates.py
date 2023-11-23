import re

date_input = input()

pattern = "\\d{2}\\/[A-Z]{1}[a-z]{2}\\/\\d{4}|\\d{2}\\.[A-Z]{1}[a-z]{2}\\.\\d{4}|\\d{2}\\-[A-Z]{1}[a-z]{2}\\-\\d{4}"

matches = re.findall(pattern, date_input)

for info in matches:
    if "/" in info:
        day, month, year = info.split("/")
        print(f"Day: {day}, Month: {month}, Year: {year}")
    elif "-" in info:
        day, month, year = info.split("-")
        print(f"Day: {day}, Month: {month}, Year: {year}")
    elif "." in info:
        day, month, year = info.split(".")
        print(f"Day: {day}, Month: {month}, Year: {year}")
