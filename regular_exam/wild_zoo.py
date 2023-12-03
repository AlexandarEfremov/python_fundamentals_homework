animal_dict = {}

while True:
    input_command = input()
    if input_command == "EndDay":
        break
    if "Add: " in input_command:
        rest_command = input_command.replace("Add: ", "")
        rest_command = rest_command.split("-")
        animal_name, needed_food_quantity, area = rest_command[0], int(rest_command[1]), rest_command[2]
        if animal_name in animal_dict:
            animal_dict[animal_name]["needed food"] += needed_food_quantity
        else:
            animal_dict[animal_name] = {"needed food": needed_food_quantity, "area": area}
    elif "Feed: " in input_command:
        rest_command = input_command.replace("Feed: ", "")
        rest_command = rest_command.split("-")
        animal_name, food = rest_command[0], int(rest_command[1])
        if animal_name in animal_dict:
            animal_dict[animal_name]["needed food"] -= food
            if animal_dict[animal_name]["needed food"] <= 0:
                print(f"{animal_name} was successfully fed")
                del animal_dict[animal_name]

print("Animals:")
for key, value in animal_dict.items():
    print(f" {key} -> {animal_dict[key]['needed food']}g")

print("Areas with hungry animals:")
area_counts = {}
for key, value in animal_dict.items():
    area = animal_dict[key]['area']
    if area in area_counts:
        area_counts[area] += 1
    else:
        area_counts[area] = 1

for area, count in area_counts.items():
    print(f" {area}: {count}")