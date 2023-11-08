amount_of_cars = int(input())
car_dict = {}


for _ in range(amount_of_cars):
    user_input = input().split()
    if "register" in user_input:
        username = user_input[1]
        license_plate = user_input[2]
        if username in car_dict.keys():
            print(f"ERROR: already registered with plate number {car_dict[username]}")
        else:
            car_dict[username] = license_plate
            print(f"{username} registered {car_dict[username]} successfully")
    elif "unregister" in user_input:
        username = user_input[1]
        if username not in car_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            del car_dict[username]
            print(f"{username} unregistered successfully")

for key, value in car_dict.items():
    print(f"{key} => {value}")


