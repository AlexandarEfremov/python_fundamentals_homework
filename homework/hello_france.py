collection_of_items = input().split("|")
budget = float(input())

max_clothes_price = 50
max_shoes_price = 35
max_accessories_price = 20.50
train_ticket = 150

bought_items_string = ""

bought_items_prices = []
profit = 0
win = False
for item in collection_of_items:
    new_item = item.split("->")
    type_of_item = new_item[0]
    item_value = float(new_item[1])
    if type_of_item == "Clothes":
        if item_value > max_clothes_price:
            continue
        else:
            if budget >= item_value:
                budget -= item_value
                bought_items_string += f"{type_of_item}-"
                bought_items_string += f"{str(item_value)} "
            elif budget < item_value:
                continue
    elif type_of_item == "Shoes":
        if item_value > max_shoes_price:
            continue
        else:
            if budget >= item_value:
                budget -= item_value
                bought_items_string += f"{type_of_item}-"
                bought_items_string += f"{str(item_value)} "
            elif budget < item_value:
                continue
    else:
        if item_value > max_accessories_price:
            continue
        else:
            if budget >= item_value:
                budget -= item_value
                bought_items_string += f"{type_of_item}-"
                bought_items_string += f"{str(item_value)} "
            elif budget < item_value:
                continue
    if budget < 0:
        break
MEGA_list = bought_items_string.split(" ")
for item in MEGA_list:
    if item == "":
        continue
    split_items = item.split("-")
    item_type = split_items[0]
    item_price = float(split_items[1])
    if item_type == "Clothes":
        markup_item_value = item_price * 1.4
        profit += markup_item_value - item_price
        budget += markup_item_value
        bought_items_prices.append(f"{markup_item_value:.2f}")
        if budget >= train_ticket:
            win = True
            break
    elif item_type == "Shoes":
        markup_item_value = item_price * 1.4
        profit += markup_item_value - item_price
        budget += markup_item_value
        bought_items_prices.append(f"{markup_item_value:.2f}")
        if budget >= train_ticket:
            win = True
            break
    else:
        markup_item_value = item_price * 1.4
        profit += markup_item_value - item_price
        budget += markup_item_value
        bought_items_prices.append(f"{markup_item_value:.2f}")
        if budget >= train_ticket:
            win = True
            break
result = " ".join(bought_items_prices)
print(result)
print(f"Profit: {profit:.2f}")
if win:
    print("Hello, France!")
else:
    print("Not enough money.")



# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60