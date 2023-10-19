pirate_ship_sections = [int(digi) for digi in input().split(">")]
pirate_ship_sections_copy = pirate_ship_sections.copy()
warship_sections = [int(digi) for digi in input().split(">")]
warship_sections_copy = warship_sections.copy()
max_health = int(input())


def fire_command(index, damage):
    if 0 <= index < len(warship_sections_copy):
        if warship_sections_copy[index] - damage > 0:
            warship_sections_copy[index] -= damage
        else:
            print("You won! The enemy ship has sunken.")
            exit()


def defend_command(start_index, end_index, damage):
    if 0 <= start_index < len(pirate_ship_sections_copy) and 0 <= end_index < len(pirate_ship_sections_copy):
        for index in range(start_index, end_index + 1):
            if pirate_ship_sections_copy[index] - damage < 0:
                print("You lost! The pirate ship has sunken.")
                exit()
            else:
                pirate_ship_sections_copy[index] -= damage


def repair_command(index, health):
    if 0 <= index < len(pirate_ship_sections_copy):
        if pirate_ship_sections_copy[index] + health > max_health:
            pirate_ship_sections_copy[index] = max_health
        else:
            pirate_ship_sections_copy[index] += health


def status_command():
    sections_needing_repair = 0
    for section in pirate_ship_sections_copy:
        if section < max_health * 0.2:
            sections_needing_repair += 1
    final_statement = f"{sections_needing_repair} sections need repair."
    return final_statement


while True:
    input_command = input()
    if input_command == "Retire":
        break
    separate_commands = input_command.split()
    if separate_commands[0] == "Fire":
        fire_command(int(separate_commands[1]), int(separate_commands[2]))
    elif separate_commands[0] == "Defend":
        defend_command(int(separate_commands[1]), int(separate_commands[2]), int(separate_commands[3]))
    elif separate_commands[0] == "Repair":
        repair_command(int(separate_commands[1]), int(separate_commands[2]))
    elif separate_commands[0] == "Status":
        status_result = status_command()
        print(status_result)


print(f"Pirate ship status: {sum(pirate_ship_sections_copy)}")
print(f"Warship status: {sum(warship_sections_copy)}")
