# Write a program that keeps the information about products and their prices. Each product has a name, a price, and
# a quantity:
#  If the product doesn't exist yet, add it with its starting quantity.
#  If you receive a product, which already exists, increases its quantity by the input quantity and if its price is
# different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep
# adding items. Finally, print all items with their names and the total price of each product.

product_dict = {}

while True:
    input_order = input()
    if input_order == "buy":
        break
    name, price, quantity = input_order.split()
    price = float(price)
    quantity = int(quantity)
    if name in product_dict.keys():
        product_dict[name]["quantity"] += quantity
        if price != product_dict[name]["price"]:
            product_dict[name]["price"] = price
    else:
        product_dict[name] = {"price": price, "quantity": quantity}

for key, value in product_dict.items():
    total_price = value["price"] * value["quantity"]
    print(f"{key} -> {total_price:.2f}")