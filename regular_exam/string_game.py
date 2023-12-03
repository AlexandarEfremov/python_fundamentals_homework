initial_string = input()

while True:
    input_command = input()
    if input_command == "Done":
        break
    input_action = input_command.split()
    if input_action[0] == "Change":
        char_to_be_changed = input_action[1]
        replacement = input_action[2]
        while char_to_be_changed in initial_string:
            initial_string = initial_string.replace(char_to_be_changed, replacement)
        print(initial_string)
    elif input_action[0] == "Includes":
        substring = input_action[1]
        is_included = False
        if substring in initial_string:
            is_included = True
        if is_included:
            print("True")
        else:
            print("False")
    elif input_action[0] == "End":
        substring = input_action[1]
        substring_length = len(substring)
        ending_bit = initial_string[-substring_length:]
        if substring == ending_bit:
            print("True")
        else:
            print("False")
    elif input_action[0] == "Uppercase":
        initial_string = initial_string.upper()
        print(initial_string)
    elif input_action[0] == "FindIndex":
        searched_char = input_action[1]
        index = initial_string.find(searched_char)
        print(index)
    elif input_action[0] == "Cut":
        start_index = int(input_action[1])
        count = int(input_action[2])
        new_string = initial_string[start_index:start_index + count]
        print(new_string)