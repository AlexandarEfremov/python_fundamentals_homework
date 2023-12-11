number_of_inputs = int(input())
import re

for _ in range(number_of_inputs):
    raw_input = input()
    pattern = r"([A-Z][a-z]{2,}\s[A-Z][a-z]{2,})#+(([A-Z][a-z]+)&?([A-Z][a-z]+)?&?([A-Z][a-z]+)?)\d{2}([A-Z][" \
              r"A-Za-z0-9]+\s(JSC|Ltd\.))"
    match = re.match(pattern, raw_input)
    if match:
        name = match.group(1)
        job_position = match.group(2)
        if "&&" in job_position:
            continue
        elif "&" in job_position:
            job_position = job_position.replace("&", " ")
        else:
            continue
        company_name = match.group(6)
        print(f"{name} is {job_position} at {company_name}")



