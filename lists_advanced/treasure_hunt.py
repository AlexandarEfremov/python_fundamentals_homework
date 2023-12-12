initial_loot = [item for item in input().split("|")]
copy_list = initial_loot.copy()

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    elif command[0] == "Loot":
        command.remove("Loot")
        for loot in command:
            if loot in copy_list:
                continue
            else:
                copy_list.insert(0, loot)
    elif command[0] == "Drop":
        index = int(command[1])
        if len(copy_list) - 1 >= index >= 0:
            dropped_loot = copy_list.pop(index)
            copy_list.append(dropped_loot)
        else:
            continue
    elif command[0] == "Steal":
        count = int(command[1])
        stolen_items = []
        if count > len(copy_list):
            stolen_items = copy_list
            copy_list = []
            print(", ".join(stolen_items))
        else:
            for item in range(count):
                last_item = copy_list.pop()
                stolen_items.append(last_item)
            stolen_items.reverse()
            print(", ".join(stolen_items))
            stolen_items = []

if len(copy_list) == 0:
    print("Failed treasure hunt.")
else:
    treasure_math = sum([len(item) for item in copy_list])
    average_gain = treasure_math / len(copy_list)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

