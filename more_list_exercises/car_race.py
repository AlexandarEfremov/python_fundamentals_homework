times_input = input().split(" ")
half_time_index = len(times_input) // 2
left_car_times = times_input[:half_time_index]
right_car_times = times_input[half_time_index + 1:]
right_car_times.reverse()

left_sum = 0
right_sum = 0

for number in left_car_times:
    number_as_int = int(number)
    left_sum += number_as_int
    if number_as_int == 0:
        left_sum *= 0.8
for number in right_car_times:
    number_as_int = int(number)
    right_sum += number_as_int
    if number_as_int == 0:
        right_sum *= 0.8

if left_sum < right_sum:
    print(f"The winner is left with total time: {left_sum:.1f}")
else:
    print(f"The winner is right with total time: {right_sum:.1f}")
