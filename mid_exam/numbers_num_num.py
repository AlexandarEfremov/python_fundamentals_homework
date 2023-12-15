integer_list = [int(digi) for digi in input().split()]
copy_list = integer_list.copy()

average_number = sum(integer_list) / len(integer_list)

greater_numbers = [num for num in copy_list if num > average_number]

sorted_numbers = sorted(greater_numbers, reverse=True)

if len(sorted_numbers) <= 0:
    print("No")

else:
    for index, num in enumerate(sorted_numbers):
        if index == 5:
            break
        print(num, end=" ")





