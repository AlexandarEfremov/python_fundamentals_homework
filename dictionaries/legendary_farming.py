items_dict = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
current_input = input().split()

while not obtained:
    for i in range(0, len(current_input), 2):
        key = current_input[i + 1].lower()
        value = int(current_input[i])
        if key not in items_dict.keys():
            items_dict[key] = 0
            items_dict[key] += value
        else:
            items_dict[key] += value
        if items_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            obtained = True
            items_dict["shards"] -= 250
        elif items_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            obtained = True
            items_dict["fragments"] -= 250
        elif items_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            obtained = True
            items_dict["motes"] -= 250
        if obtained:
            break
    if obtained:
        break
    current_input = input().split()

for material, quantity in items_dict.items():
    print(f"{material}: {quantity}")

# 3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards
# 123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver
