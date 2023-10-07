fire_cells = input().split("#")
water = int(input())

effort = 0
total_fire = 0
extinguished_cells = []

for item in fire_cells:
    split_item = item.split(" = ")
    type_of_fire = split_item[0]
    range_of_fire = int(split_item[1])
    if type_of_fire == "High" and 81 <= range_of_fire <= 125:
        if water >= range_of_fire:
            water -= range_of_fire
            current_effort = range_of_fire / 4
            effort += current_effort
            total_fire += range_of_fire
            extinguished_cells.append(range_of_fire)
        else:
            continue
    elif type_of_fire == "Medium" and 51 <= range_of_fire <= 80:
        if water >= range_of_fire:
            water -= range_of_fire
            current_effort = range_of_fire / 4
            effort += current_effort
            total_fire += range_of_fire
            extinguished_cells.append(range_of_fire)
        else:
            continue
    elif type_of_fire == "Low" and 1 <= range_of_fire <= 50:
        if water >= range_of_fire:
            water -= range_of_fire
            current_effort = range_of_fire / 4
            effort += current_effort
            total_fire += range_of_fire
            extinguished_cells.append(range_of_fire)
        else:
            continue
print("Cells:")

for cell in extinguished_cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

# High = 89#Low = 28#Medium = 77#Low = 23

