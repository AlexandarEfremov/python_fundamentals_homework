force_dict = {}

while True:
    input_info = input()
    if input_info == "Lumpawaroo":
        break

    if " | " in input_info:
        force_side, force_user = input_info.split(" | ")
        if force_side not in force_dict:
            force_dict[force_side] = []
        for users in force_dict.values():
            if force_user in users:
                break
        else:
            force_dict[force_side].append(force_user)
    elif " -> " in input_info:
        force_user, force_side = input_info.split(" -> ")
        for side, users in force_dict.items():
            if force_user in users:
                users.remove(force_user)
                break
        force_dict.setdefault(force_side, []).append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, users in force_dict.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
