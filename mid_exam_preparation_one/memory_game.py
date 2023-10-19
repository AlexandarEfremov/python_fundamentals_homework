elements_sequence = [digi for digi in input().split()]
working_list = elements_sequence.copy()

moves_until_now = 0


while len(working_list) > 0:
    moves_until_now += 1
    input_command = input().split()
    if input_command[0] == "end":
        break
    else:
        first_index = input_command[0]
        second_index = input_command[1]
        if int(first_index) == int(second_index) or int(first_index) < 0 or int(second_index) < 0 or int(first_index) \
                > len(working_list) - 1 or int(second_index) > len(working_list) - 1:
            halved_list = int(len(working_list) / 2)
            first_additional = f"-{moves_until_now}a"
            second_additional = f"-{moves_until_now}a"
            working_list = working_list[:halved_list] + [str(first_additional)] + [str(second_additional)] + working_list[halved_list:]
            print("Invalid input! Adding additional elements to the board")
        else:
            if working_list[int(first_index)] == working_list[int(second_index)]:
                print(f"Congrats! You have found matching elements - {working_list[int(first_index)]}!")
                value_to_remove = working_list[int(first_index)]
                working_list.remove(value_to_remove)
                working_list.remove(value_to_remove)
            else:
                print("Try again!")


if len(working_list) > 0:
    print(f"Sorry you lose :(")
    joined_list = " ".join(working_list)
    print(joined_list)
else:
    print(f"You have won in {moves_until_now} turns!")