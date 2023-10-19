shopping_list = input().split("!")
working_list = shopping_list.copy()

while True:
    input_command = input().split()
    if " ".join(input_command) == "Go Shopping!":
        break
    if input_command[0] == "Urgent":
        item_type = input_command[1]
        if item_type in working_list:
            continue
        else:
            working_list.insert(0, item_type)
    elif input_command[0] == "Unnecessary":
        removed_item = input_command[1]
        if removed_item not in working_list:
            continue
        else:
            working_list.remove(removed_item)
    elif input_command[0] == "Correct":
        old_name = input_command[1]
        new_name = input_command[2]
        if old_name not in working_list:
            continue
        else:
            old_name_index = working_list.index(old_name)
            working_list.remove(old_name)
            working_list.insert(old_name_index, new_name)
    elif input_command[0] == "Rearrange":
        item_type = input_command[1]
        if item_type not in working_list:
            continue
        else:
            item_type_index = working_list.index(item_type)
            popped_item = working_list.pop(item_type_index)
            working_list.append(popped_item)

print(", ".join(working_list))
