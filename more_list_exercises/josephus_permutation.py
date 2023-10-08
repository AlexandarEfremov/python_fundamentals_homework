initial_number = input().split(" ")
step = int(input())
idx = 0
removed_list = []
while len(initial_number) > 0:
    idx = (idx + step - 1) % len(initial_number)
    removed_list.append(initial_number.pop(idx))
print(f"[{','.join(removed_list)}]")



