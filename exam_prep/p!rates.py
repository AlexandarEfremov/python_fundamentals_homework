plunder_dict = {}

while True:
    input_info = input()
    if input_info == "Sail":
        break
    city = input_info.split("||")[0]
    population = int(input_info.split("||")[1])
    gold = int(input_info.split("||")[2])
    if city not in plunder_dict:
        plunder_dict[city] = [population, gold]
    else:
        plunder_dict[city][0] += population
        plunder_dict[city][1] += gold

while True:
    event_command = input()
    if event_command == "End":
        break
    if "Plunder" in event_command:
        city = event_command.split("=>")[1]
        people = int(event_command.split("=>")[2])
        gold = int(event_command.split("=>")[3])
        plunder_dict[city][0] -= people
        plunder_dict[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if plunder_dict[city][0] <= 0 or plunder_dict[city][1] <= 0:
            print(f"{city} has been wiped off the map!")
            del plunder_dict[city]
    elif "Prosper" in event_command:
        city = event_command.split("=>")[1]
        gold = int(event_command.split("=>")[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            plunder_dict[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {plunder_dict[city][1]} gold.")

if plunder_dict:
    print(f"Ahoy, Captain! There are {len(plunder_dict.keys())} wealthy settlements to go to:")
    for key, value in plunder_dict.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
