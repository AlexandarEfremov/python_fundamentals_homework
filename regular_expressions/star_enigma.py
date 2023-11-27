import re

number_of_lines = int(input())

attacked_planets = []
destroyed_planets = []

for i in range(number_of_lines):
    key_pattern = r"[SsTtAaRr]"
    input_line = input()
    match = re.findall(key_pattern, input_line)
    match_length = len(match)
    decrypted_line = ""
    for char in input_line:
        char = chr(ord(char) - match_length)
        decrypted_line += char
    new_pattern = r"[^\@\-\!\:\>]*?@([A-Za-z]+)[^\@\-\!\:\>]*?(:([\d+]+))[^\@\-\!\:\>]*?!([(A|D)])![^\@\-\!\:\>]*?->([0-9]+)"
    new_match = re.search(new_pattern, decrypted_line)
    if new_match:
        planet_name = new_match.group(1)
        planet_population = new_match.group(3)
        attack_type = new_match.group(4)
        soldier_count = new_match.group(5)

        if attack_type == "A" or attack_type == "a":
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)


sorted_attacked = list(sorted(attacked_planets))
sorted_destroyed = list(sorted(destroyed_planets))

len_attacked = len(sorted_attacked)
len_destroyed = len(sorted_destroyed)

print(f"Attacked planets: {len_attacked}")
for i in sorted_attacked:
    print(f"-> {i}")
print(f"Destroyed planets: {len_destroyed}")
for j in sorted_destroyed:
    print(f"-> {j}")