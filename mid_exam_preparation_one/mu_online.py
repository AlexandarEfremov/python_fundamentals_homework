initial_health = 100
initial_bitcoin = 0
room_input_string = input().split("|")
best_room = 0


def health_potion(hp_amount, initial_health):
    diff = 100 - initial_health
    if initial_health + hp_amount < 100:
        updated_health = initial_health + hp_amount
        print(f"You healed for {hp_amount} hp.")
        print(f"Current health: {updated_health} hp.")
        return updated_health
    else:
        updated_health = 100
        print(f"You healed for {diff} hp.")
        print(f"Current health: {updated_health} hp.")
        return updated_health


def found_bitcoin(bitcoins, initial_bitcoin):
    initial_bitcoin += bitcoins
    print(f"You found {bitcoins} bitcoins.")
    return initial_bitcoin


def monster_attack(attack_strength, initial_health, monster_name, best_room):
    updated_health = initial_health - attack_strength
    if updated_health <= 0:
        print(f"You died! Killed by {monster_name}.")
        print( f"Best room: {best_room}")
        exit()
    else:
        print(f"You slayed {monster_name}.")
        return updated_health


for i in room_input_string:

    room_types = i.split()
    room_encounter = room_types[0]
    room_value = room_types[1]
    best_room += 1
    if room_encounter == "potion":
        initial_health = health_potion(int(room_value), initial_health)
    elif room_encounter == "chest":
        initial_bitcoin = found_bitcoin(int(room_value), initial_bitcoin)
    else:
        initial_health = monster_attack(int(room_value), initial_health, room_encounter, best_room)

if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")

# cat 10|potion 30|orc 10|chest 10|snake 25|chest 110