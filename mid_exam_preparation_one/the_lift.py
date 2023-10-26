# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next
# one with space available.

people_waiting = int(input())
current_state = [int(digi) for digi in input().split(" ")]
seating_list = []
max_occupancy = 4
leftover = 0

total_available_seats = 0

for seat in current_state:
    if seat >= 4:
        seating_list.append(max_occupancy)
        continue
    else:
        diff = 4 - seat
        total_available_seats += diff

for lift_car in current_state:
    if people_waiting >= 4:
        if lift_car >= 4:
            continue
        elif lift_car == 0:
            seating_list.append(max_occupancy)
            people_waiting -= 4
        else:
            available_lift_car_seats = 4 - lift_car
            if people_waiting <= available_lift_car_seats:
                diff = people_waiting
                seating_list.append(lift_car + people_waiting)
                people_waiting -= diff
            elif people_waiting > available_lift_car_seats:
                if people_waiting >= 4:
                    occupied_seats = 4 - lift_car
                    people_waiting -= occupied_seats
                    seating_list.append(max_occupancy)
                elif people_waiting < 4:
                    available_seats = 4 - lift_car
                    diff = people_waiting - available_seats
                    if diff <= available_seats:
                        people_waiting -= diff
                        seating_list.append(lift_car + diff)
                    elif diff > available_seats:
                        leftover_people = abs(diff - available_seats)
                        seating_list.append(max_occupancy)
                        leftover += leftover_people
    else:
        available_lift_car_seats = 4 - lift_car
        if people_waiting <= available_lift_car_seats:
            diff = people_waiting
            seating_list.append(lift_car + people_waiting)
            people_waiting -= diff
        elif people_waiting > available_lift_car_seats:
            leftover_people = people_waiting - available_lift_car_seats
            leftover += leftover_people
            seating_list.append(max_occupancy)

seating_str = [str(st) for st in seating_list]
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting - leftover} people in a queue!")
    print(" ".join(seating_str))
else:
    print(f"The lift has empty spots!")
    print(" ". join(seating_str))





