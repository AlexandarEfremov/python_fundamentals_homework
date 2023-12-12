index_string = [int(digi) for digi in input().split()]
copy_list = index_string.copy()
shot_targets = 0

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index <= len(copy_list) - 1:
        shot_targets += 1
        number_at_index = copy_list[index]
        copy_list[index] = -1
        for indx, number in enumerate(copy_list):
            if number == -1:
                continue
            elif number > number_at_index:
                copy_list[indx] = number - number_at_index
            else:
                copy_list[indx] = number + number_at_index
    else:
        continue

copy_list = map(str, copy_list)
print(f"Shot targets: {shot_targets} -> {' '.join(copy_list)}")
