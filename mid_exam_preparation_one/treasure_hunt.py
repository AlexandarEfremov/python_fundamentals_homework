initial_loot = [loot for loot in input().split("|")]
initial_loot_copy = initial_loot.copy()


while True:
    initial_command = input()
    if initial_command == "Yohoho!":
        break
    command_element = initial_command.split()
    if command_element[0] == "Loot":
        command_element.remove("Loot")
        new_loot = command_element.copy()
        for loot in new_loot:
            if loot in initial_loot:
                continue
            else:
                initial_loot_copy.insert(0, loot)
    elif command_element[0] == "Drop":
        index_value = int(command_element[1])
        if 0 <= index_value < len(initial_loot_copy):
            dropped_loot = initial_loot_copy.pop(int(command_element[1]))
            initial_loot_copy.append(dropped_loot)
        else:
            continue
    elif command_element[0] == "Steal":
        stolen_items = int(command_element[1])
        stolen_stuff = [stol for stol in initial_loot_copy[-stolen_items:]]
        print(", ".join(stolen_stuff))
        for item in range(stolen_items):
            initial_loot_copy.pop()


treasure_sum = 0
total_items = 0

for item in initial_loot_copy:
    len_of_item = len(item)
    treasure_sum += len_of_item
    total_items += 1


if treasure_sum <= 0:
    print("Failed treasure hunt.")
else:
    average_gain = treasure_sum / total_items
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")




