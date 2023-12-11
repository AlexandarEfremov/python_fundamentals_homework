raw_activation_key = input()

while True:
    input_command = input()
    if input_command == "Generate":
        break
    action = input_command.split(">>>")
    if action[0] == "Contains":
        substring = action[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action[0] == "Flip":
        if action[1] == "Upper":
            start_index = int(action[2])
            end_index = int(action[3])
            new_string = raw_activation_key[start_index:end_index]
            manipulated_string = new_string.upper()
            raw_activation_key = raw_activation_key.replace(new_string, manipulated_string)
            print(raw_activation_key)
        elif action[1] == "Lower":
            start_index = int(action[2])
            end_index = int(action[3])
            new_string = raw_activation_key[start_index:end_index]
            manipulated_string = new_string.lower()
            raw_activation_key = raw_activation_key.replace(new_string, manipulated_string)
            print(raw_activation_key)
    elif action[0] == "Slice":
        start_index = int(action[1])
        end_index = int(action[2])
        new_string = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(new_string, "")
        print(raw_activation_key)

print(f"Your activation key is: {raw_activation_key}")
