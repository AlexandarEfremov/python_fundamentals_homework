food_dict = {}
total_sales = 0

while True:
    input_info = input()
    if input_info == "Complete":
        break
    command = input_info.split()
    if command[0] == "Receive":
        quantity = int(command[1])
        food = command[2]
        if food not in food_dict:
            food_dict[food] = quantity
        else:
            if quantity > 0:
                food_dict[food] += quantity
    elif command[0] == "Sell":
        quantity = int(command[1])
        food = command[2]
        if food not in food_dict:
            print(f"You do not have any {food}.")
        elif food_dict[food] > quantity:
            food_dict[food] -= quantity
            print(f"You sold {quantity} {food}.")
            total_sales += quantity
        elif food_dict[food] == quantity:
            print(f"You sold {quantity} {food}.")
            total_sales += quantity
            del food_dict[food]
        elif food_dict[food] < quantity:
            available_food = food_dict[food]
            total_sales += available_food
            print(f"There aren't enough {food}. You sold the last {available_food} of them.")
            del food_dict[food]

for key, value in food_dict.items():
    print(f"{key}: {value}")
print(f"All sold: {total_sales} goods")

