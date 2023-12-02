concealed_message = input()

while True:
    input_command = input()
    if input_command == "Reveal":
        break
    action = input_command.split( ":|:")
    if action[0] == "InsertSpace":
        index = int(action[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action[0] == "Reverse":
        substring = action[1]
        if substring in concealed_message:
            reversed_substring = substring[::-1]
            concealed_message = concealed_message.replace(substring, reversed_substring)
            print(concealed_message)
        else:
            print("error")
    elif action[0] == "ChangeAll":
        substring = action[1]
        replacement = action[2]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")