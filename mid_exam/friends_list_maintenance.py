friends_list = input().split(", ")
blacklisted_names = 0
lost_names = 0
blacklist = []

while True:
    input_command = input()
    if input_command == "Report":
        break
    specific_command = input_command.split()
    if specific_command[0] == "Blacklist":
        blacklisted_name = specific_command[1]
        if blacklisted_name in friends_list:
            blacklisted_name_index = friends_list.index(blacklisted_name)
            friends_list[blacklisted_name_index] = "Blacklisted"
            blacklisted_names += 1
            blacklist.append(blacklisted_name)
            print(f"{blacklisted_name} was blacklisted.")
        else:
            print(f"{blacklisted_name} was not found.")
    elif specific_command[0] == "Error":
        error_index = int(specific_command[1])
        if 0 <= error_index < len(friends_list) and friends_list[error_index] != "Blacklisted" and friends_list[error_index] != "Lost":
            lost_name = friends_list[error_index]
            friends_list[error_index] = "Lost"
            lost_names += 1
            print(f"{lost_name} was lost due to an error.")
    elif specific_command[0] == "Change":
        change_index = int(specific_command[1])
        new_name = specific_command[2]
        if 0 <= change_index < len(friends_list):
            current_name = friends_list[change_index]
            friends_list[change_index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(friends_list))