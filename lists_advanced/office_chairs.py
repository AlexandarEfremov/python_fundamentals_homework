number_of_rooms = int(input())


def check_the_room(num_of_rooms):
    free_chairs = 0
    for i in range(1, number_of_rooms + 1):
        chair_amount, visitor_amount = input().split()
        diff = len(chair_amount) - int(visitor_amount)
        if diff < 0:
            print(f"{abs(diff)} more chairs needed in room {i}")
        free_chairs += diff
    return free_chairs


total_free_chairs = check_the_room(number_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")



