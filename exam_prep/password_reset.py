info_string = input()

while True:
    command_input = input()
    if command_input == "Done":
        break

    if "TakeOdd" in command_input:
        string = [char for index, char in enumerate(info_string) if index % 2 != 0]
        info_string = "".join(string)
        print(info_string)

    elif "Cut" in command_input:
        index = int(command_input.split()[1])
        length = int(command_input.split()[2])
        info_string = info_string[:index] + info_string[index + length:]
        print(info_string)

    elif "Substitute" in command_input:
        substring = command_input.split()[1]
        substitute = command_input.split()[2]
        if substring in info_string:
            info_string = info_string.replace(substring, substitute)
            print(info_string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {info_string}")
