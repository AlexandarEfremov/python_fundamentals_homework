number_of_heroes = int(input())
hero_dict = {}

for _ in range(number_of_heroes):
    hero_info = input()
    hero, hp, mp = hero_info.split()[0], int(hero_info.split()[1]), int(hero_info.split()[2])
    if hero not in hero_dict:
        hero_dict[hero] = {"hp": hp, "mp": mp}

while True:
    input_command = input()
    if input_command == "End":
        break
    if "CastSpell" in input_command:
        hero, mp_needed, spell_name = input_command.split(" - ")[1], int(input_command.split(" - ")[2]), \
                                      input_command.split(" - ")[3]
        if hero_dict[hero]["mp"] >= mp_needed:
            hero_dict[hero]["mp"] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {hero_dict[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif "TakeDamage" in input_command:
        hero, damage, attacker = input_command.split(" - ")[1], int(input_command.split(" - ")[2]), \
                                      input_command.split(" - ")[3]
        hero_dict[hero]["hp"] -= damage
        if hero_dict[hero]["hp"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {hero_dict[hero]['hp']} HP left!")
        else:
            del hero_dict[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif "Recharge" in input_command:
        hero, amount = input_command.split(" - ")[1], int(input_command.split(" - ")[2])
        if hero_dict[hero]["mp"] + amount > 200:
            diff = 200 - hero_dict[hero]["mp"]
            hero_dict[hero]["mp"] = 200
            print(f"{hero} recharged for {diff} MP!")
        else:
            hero_dict[hero]["mp"] += amount
            print(f"{hero } recharged for {amount} MP!")

    elif "Heal" in input_command:
        hero, amount = input_command.split(" - ")[1], int(input_command.split(" - ")[2])
        if hero_dict[hero]["hp"] + amount > 100:
            diff = 100 - hero_dict[hero]["hp"]
            hero_dict[hero]["hp"] = 100
            print(f"{hero} healed for {diff} HP!")
        else:
            hero_dict[hero]["hp"] += amount
            print(f"{hero} healed for {amount} HP!")

for key, value in hero_dict.items():
    print(f"{key}\n  HP: {value['hp']}\n  MP: {value['mp']}")
