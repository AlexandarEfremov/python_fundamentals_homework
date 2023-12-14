integer_list = [int(digi) for digi in input().split()]
copy_list = integer_list.copy()

while True:
    command = input().split()
    if command[0] == "end":
        break
    elif command[0] == "swap":
        index_one = int(command[1])
        index_two = int(command[2])
        if 0 <= index_one < len(copy_list) and 0 <= index_two < len(copy_list):
            copy_list[index_one], copy_list[index_two] = copy_list[index_two], copy_list[index_one]
    elif command[0] == "multiply":
        index_one = int(command[1])
        index_two = int(command[2])
        copy_list[index_one] = copy_list[index_one] * copy_list[index_two]
    elif command[0] == "decrease":
        copy_list = [int(digi) - 1 for digi in copy_list]

print(", ".join(map(str, copy_list)))
