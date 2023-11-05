# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command
# "statistics". Sometimes you may receive a product more than once. In that case, you have to add the new
# quantity to the existing one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

input_command = input()
my_dict = {}
product_counter = 0
value_counter = 0
while input_command != "statistics":
    product = input_command.split(":")[0]
    value = input_command.split(":")[1]
    if product not in my_dict:
        my_dict[product] = int(value)
        value_counter += int(value)
        product_counter += 1
    else:
        my_dict[product] += int(value)
        value_counter += int(value)
    input_command = input()

print(f"Products in stock:")
for item, value in my_dict.items():
    print(f"- {item}: {value}")
print(f"""Total Products: {product_counter}
Total Quantity: {value_counter}""")