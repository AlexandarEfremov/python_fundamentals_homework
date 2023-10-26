price_rating = [int(digi) for digi in input().split(", ")]
entry_point = int(input())
type_of_items = input()

left_sum = 0
right_sum = 0

if type_of_items == "cheap":
    for i in range(entry_point):
        if price_rating[i] < price_rating[entry_point]:
            left_sum += price_rating[i]
    for i in range(entry_point + 1, len(price_rating)):
        if price_rating[i] < price_rating[entry_point]:
            right_sum += price_rating[i]
elif type_of_items == "expensive":
    for i in range(entry_point):
        if price_rating[i] >= price_rating[entry_point]:
            left_sum += price_rating[i]
    for i in range(entry_point + 1, len(price_rating)):
        if price_rating[i] >= price_rating[entry_point]:
            right_sum += price_rating[i]

if left_sum > right_sum:
    print(f"Left - {left_sum}")
elif left_sum < right_sum:
    print(f"Right - {right_sum}")
else:
    print(f"Left - {left_sum}")
