import re
income = 0
while True:
    input_info = input()
    if input_info == "end of shift":
        break
    pattern = r"\%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[^\|\$\%\.]*?([1-9]+[.0-9]*)\$"
    match = re.search(pattern, input_info)
    if match:
        customer, product, count, price = match.groups()
        current_income = float(count) * float(price)
        income += current_income
        print(f"{customer}: {product} - {current_income:.2f}")
print(f"Total income: {income:.2f}")





