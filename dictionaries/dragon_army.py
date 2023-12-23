number_of_dragons = int(input())
dragon_dict = {}


def adding_info(dr_type, dr_name, dr_damage, dr_health, dr_armor):
    dragon_dict[dr_type] = dragon_dict.get(dr_type, {})
    dragon_dict[dr_type][dr_name] = dragon_dict[dr_type].get(dr_name, {"damage": dr_damage, "health": dr_health,
                                                                       "armor": dr_armor})


for _ in range(number_of_dragons):
    input_info = input().split()
    if input_info[2] == "null":
        damage = 45
        dragon_type, name, health, armor = input_info[0], input_info[1], int(input_info[3]), int(input_info[4])
        adding_info(dragon_type, name, damage, health, armor)
    elif input_info[3] == "null":
        health = 250
        dragon_type, name, damage, armor = input_info[0], input_info[1], int(input_info[2]), int(input_info[4])
        adding_info(dragon_type, name, damage, health, armor)
    elif input_info[4] == "null":
        armor = 10
        dragon_type, name, damage, health = input_info[0], input_info[1], int(input_info[2]), int(input_info[3])
        adding_info(dragon_type, name, damage, health, armor)
    else:
        dragon_type, name, damage, health, armor = (input_info[0], input_info[1], int(input_info[2]),
                                                    int(input_info[3]), int(input_info[4]))
        adding_info(dragon_type, name, damage, health, armor)


def average_dmg_hlt_arm(stats):
    total_damage = 0
    total_health = 0
    total_armor = 0
    if stats:
        for dragon_name, dragon_stats in stats.items():
            total_damage += dragon_stats["damage"]
            total_health += dragon_stats["health"]
            total_armor += dragon_stats["armor"]

        average_damage = total_damage / len(stats)
        average_health = total_health / len(stats)
        average_armor = total_armor / len(stats)

        return f"({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})"
    else:
        return "(0.00/0.00/0.00)"


for key, value in dragon_dict.items():
    print(f"{key}::{average_dmg_hlt_arm(value)}")
    sorted_dragons = dict(sorted(value.items(), key=lambda x: x[0]))

    for name, stats in sorted_dragons.items():
        damage = stats["damage"]
        health = stats["health"]
        armor = stats["armor"]
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")
