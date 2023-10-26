price_without_tax = 0
special_cond = False
while True:
    input_command = input()
    if input_command == "special":
        special_cond = True
    if input_command == "special" or input_command == "regular":
        break
    if float(input_command) < 0:
        print("Invalid price!")
        continue
    price_without_tax += float(input_command)


total_taxes = price_without_tax * 0.2
total_price = price_without_tax + total_taxes

if total_price == 0:
    print("Invalid order!" )
else:
    if special_cond:
        new_price = total_price * 0.9
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_tax:.2f}$")
        print(f"Taxes: {total_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {new_price:.2f}$")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_tax:.2f}$")
        print(f"Taxes: {total_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")