initial_string = input()
temp_string = initial_string


def add_stop(in_string, indx, str_to_add):
    if indx <= len(in_string) - 1:
        new_string = in_string[:indx] + str_to_add + in_string[indx:]
        return new_string
    else:
        return in_string


def remove_stop(in_string, start, end):
    if start <= len(in_string) - 1 and end <= len(in_string) - 1:
        str_to_be_removed = in_string[start:end + 1]
        new_str = in_string.replace(str_to_be_removed, "")
        return new_str
    else:
        return in_string


def switch(in_string, old_str, new_str):
    if old_str in in_string:
        new_string = in_string.replace(old_str, new_str)
        return new_string
    else:
        return in_string


while True:
    input_command = input()
    if input_command == "Travel":
        print(f"Ready for world tour! Planned stops: {temp_string}")
        break
    if "Add Stop" in input_command:
        index = int(input_command.split(":")[1])
        string = input_command.split(":")[2]
        temp_string = add_stop(temp_string, index, string)
        print(temp_string)
    elif "Remove Stop" in input_command:
        start_index = int(input_command.split(":")[1])
        end_index = int(input_command.split(":")[2])
        temp_string = remove_stop(temp_string, start_index, end_index)
        print(temp_string)
    elif "Switch" in input_command:
        old_string = input_command.split(":")[1]
        new_string = input_command.split(":")[2]
        temp_string = switch(temp_string, old_string, new_string)
        print(temp_string)
