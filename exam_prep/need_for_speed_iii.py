number_of_cars = int(input())
car_dict = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    car_dict[car] = [mileage, fuel]
while True:
    input_command = input()
    if input_command == "Stop":
        break
    if "Drive" in input_command:
        car = input_command.split(" : ")[1]
        distance = int(input_command.split(" : ")[2])
        fuel_to_spend = int(input_command.split(" : ")[3])
        if car_dict[car][1] < fuel_to_spend:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car][1] -= fuel_to_spend
            car_dict[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel_to_spend} liters of fuel consumed.")
        if car_dict[car][0] >= 100000:
            del car_dict[car]
            print(f"Time to sell the {car}!")

    elif "Refuel" in input_command:
        car = input_command.split(" : ")[1]
        fuel = int(input_command.split(" : ")[2])
        if car_dict[car][1] + fuel < 75:
            car_dict[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            top_up = 75 - car_dict[car][1]
            car_dict[car][1] = 75
            print(f"{car} refueled with {top_up} liters")

    elif "Revert" in input_command:
        car = input_command.split(" : ")[1]
        kilometers = int(input_command.split(" : ")[2])
        car_dict[car][0] -= kilometers
        if car_dict[car][0] < 10000:
            car_dict[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in car_dict.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")


