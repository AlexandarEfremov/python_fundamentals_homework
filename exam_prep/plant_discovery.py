number_of_inputs = int(input())
plant_dict = {}

for _ in range(number_of_inputs):
    plant,rarity = input().split("<->")
    if plant in plant_dict:
        plant_dict[plant]['rarity'] = rarity
        continue
    plant_dict[plant] = plant_dict.get(plant, {'rarity': rarity, 'rating': []})

while True:
    input_command = input()
    if input_command == "Exhibition":
        break
    new_info = input_command.split()
    action = new_info[0]
    current_plant = new_info[1]
    if current_plant not in plant_dict:
        print("error")
        continue
    if action == "Rate:":
        rating = int(new_info[3])
        plant_dict[current_plant]['rating'].append(rating)
    elif action == "Update:":
        new_rarity = int(new_info[3])
        plant_dict[current_plant]['rarity'] = new_rarity
    elif action == "Reset:":
        plant_dict[current_plant]['rating'] = []

print("Plants for the exhibition:")

for plant in plant_dict:
    rarity = plant_dict[plant]['rarity']
    rating = 0
    if len(plant_dict[plant]['rating']):
        rating = sum(plant_dict[plant]['rating']) / len(plant_dict[plant]['rating'])
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")