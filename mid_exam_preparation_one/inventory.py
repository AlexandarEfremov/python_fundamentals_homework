collected_items = input().split(", ")
second_list = collected_items.copy()
while True:
    input_command = input()
    if input_command == "Craft!":
        break
    command = input_command.split(" - ")
    action = command[1]
    if command[0] == "Collect":
        if action in second_list:
            continue
        else:
            second_list.append(action)
    elif command[0] == "Drop":
        if action not in second_list:
            continue
        else:
            second_list.remove(action)
    elif command[0] == "Combine Items":
        new_split = action.split(":")
        old_item = new_split[0]
        new_item = new_split[1]
        if old_item not in second_list:
            continue
        else:
            old_item_index = second_list.index(old_item)
            second_list.insert(old_item_index + 1, new_item)
    elif command[0] == "Renew":
        if action not in second_list:
            continue
        else:
            second_list.remove(action)
            second_list.append(action)

print(", ".join(second_list))
