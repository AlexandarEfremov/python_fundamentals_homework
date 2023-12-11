empty_string = ""

while True:
    input_command = input()
    if input_command == "End":
        break
    command = input_command.split()
    if command[0] == "Add":
        substring = command[1]
        empty_string += substring
    elif command[0] == "Upgrade":
        character = command[1]
        while character in empty_string:
            ascii_char = chr(ord(character) + 1)
            empty_string = empty_string.replace(character, ascii_char)
    elif command[0] == "Print":
        print(empty_string)
    elif command[0] == "Index":
        chara = command[1]
        indexes = [str(index) for index, char in enumerate(empty_string) if char == chara]
        if len(indexes) == 0:
            print("None")
        else:
            print(" ".join(indexes))
    elif command[0] == "Remove":
        sub_string = command[1]
        while sub_string in empty_string:
            empty_string = empty_string.replace(sub_string, "")
