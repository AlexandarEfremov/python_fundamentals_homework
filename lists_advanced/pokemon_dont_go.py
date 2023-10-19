integer_list = [int(digi) for digi in input().split()]
current_list = integer_list.copy()
removed_elements_list = []

while len(current_list) > 0:
    index_input = int(input())
    if index_input < 0:
        secondary_removed_element = current_list.pop(0)
        removed_elements_list.append(secondary_removed_element)
        current_list.insert(0, current_list[-1])
        elements_change = [num + secondary_removed_element if num <= secondary_removed_element \
                           else num - secondary_removed_element for num in current_list]
        current_list = elements_change
    elif index_input > len(current_list) - 1:
        secondary_removed_element = current_list.pop(-1)
        removed_elements_list.append(secondary_removed_element)
        current_list.append(current_list[0])
        elements_change = [num + secondary_removed_element if num <= secondary_removed_element \
                           else num - secondary_removed_element for num in current_list]
        current_list = elements_change
    else:
        removed_element = current_list.pop(index_input)
        removed_elements_list.append(removed_element)
        elements_change = [num + removed_element if num <= removed_element else num - removed_element \
                           for num in current_list]
        current_list = elements_change

total = sum(removed_elements_list)

print(f"{total}")
