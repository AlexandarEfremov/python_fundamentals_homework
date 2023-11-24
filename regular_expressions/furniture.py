# Write a program that calculates the total cost of bought furniture. You will be given information about each
# purchase on separate lines until you receive the command "Purchase". Valid information should be in the
# format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer
# number. You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

import re
results_list = []

while True:
    input_info = input()
    if input_info == "Purchase":
        break
    pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
    result = re.findall(pattern, input_info)
    if len(result) == 0:
        continue
    results_list.append(result)

print("Bought furniture:")
total_price = 0
for sequence in results_list:
    for item in sequence:
        furniture = item[0]
        price = float(item[1])
        quantity = int(item[2])
        temp_price = price * quantity
        total_price += temp_price
        print(furniture)
print(f"Total money spend: {total_price:.2f}")

