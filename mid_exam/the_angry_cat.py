price_rating = [int(digi) for digi in input().split(", ")]
items_list = price_rating.copy()
entry_point = int(input())
type_of_items = input()

left_list = items_list[:entry_point]
right_list = items_list[entry_point + 1:]

broken_cheap_left = 0
broken_expensive_left = 0
broken_cheap_right = 0
broken_expensive_right = 0

for item in left_list:
    if type_of_items == "cheap":
        if item < entry_point:
            broken_cheap_left += item
    elif type_of_items == "expensive":
        if item >= entry_point:
            broken_expensive_left += item
for item in right_list:
    if type_of_items == "cheap":
        if item < entry_point:
            broken_cheap_right += item
    elif type_of_items == "expensive":
        if item >= entry_point:
            broken_expensive_right += item

if type_of_items == "cheap":
    if broken_cheap_left > broken_cheap_right:
        print(f"Left - {broken_cheap_left}")
    elif broken_cheap_left < broken_cheap_right:
        print(f"Right - {broken_cheap_right}")
    else:
        print(f"Left - {broken_cheap_left}")
elif type_of_items == "expensive":
    if broken_expensive_left > broken_expensive_right:
        print(f"Left - {broken_expensive_left}")
    elif broken_expensive_left < broken_expensive_right:
        print(f"Right - {broken_expensive_right}")
    else:
        print(f"Left - {broken_expensive_left}")