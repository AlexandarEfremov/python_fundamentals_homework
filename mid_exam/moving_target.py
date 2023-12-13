number_sequence = [int(digi) for digi in input().split()]
copy_list = number_sequence.copy()

while True:
    command = input().split()
    if command[0] == "End":
        print('|'.join(map(str, copy_list)))
        break
    elif command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(copy_list):
            copy_list[index] -= power
            if copy_list[index] <= 0:
                copy_list.pop(index)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(copy_list):
            copy_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        start_index = index - radius
        end_index = index + (radius + 1)
        if 0 <= start_index < len(copy_list) and 0 <= end_index <= len(copy_list):
            targets_to_remain = copy_list[:start_index] + copy_list[end_index:]
            copy_list = targets_to_remain
        else:
            print("Strike missed!")




