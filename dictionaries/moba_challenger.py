player_pool = {}

while True:
    input_info = input()
    if input_info == "Season end":
        break
    if "->" in input_info:
        player, position, skill = input_info.split("->")
        skill = int(skill)
        if player not in player_pool:
            player_pool[player] = []
            player_pool[player].append({position, skill})
        else:
            if player_pool[player][skill] < skill:
                player_pool[player][skill] = skill
    elif "vs" in input_info:
        first_player, second_player = input_info.split("vs")

print(player_pool)