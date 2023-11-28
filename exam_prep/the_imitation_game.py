encrypted_message = input()
temp_string = encrypted_message


def move_text(string, letters):
    front_split = string[:letters]
    rest = string[letters:]
    new_string = rest + front_split
    return new_string


def insert_text(string, working_index, inserted_value):
    before_insertion = string[:working_index]
    rest = string[working_index:]
    after_insertion = before_insertion + inserted_value + rest
    return after_insertion


def change_all(string, sub_string, rep_string):
    new_string = string.replace(sub_string, rep_string)
    return new_string


while True:
    input_command = input()
    if input_command == "Decode":
        break
    if "Move" in input_command:
        number_of_letters_to_move = int(input_command.split("|")[1])
        temp_string = move_text(temp_string, number_of_letters_to_move)
    elif "Insert" in input_command:
        index = int(input_command.split("|")[1])
        value = input_command.split("|")[2]
        temp_string = insert_text(temp_string, index, value)
    elif "ChangeAll" in input_command:
        substring = input_command.split("|")[1]
        replacement = input_command.split("|")[2]
        temp_string = change_all(temp_string, substring, replacement)

print(f"The decrypted message is: {temp_string}")