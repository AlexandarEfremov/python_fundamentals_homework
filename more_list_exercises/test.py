numbers = input().split(' ')
step = int(input())
counted = []
idx = 0
while len(numbers) > 0:
    new_idx = (idx + step - 1)
    second_idx = new_idx % len(numbers)
    idx = second_idx
    counted.append(numbers.pop(idx))
print(f"[{','.join(counted)}]")

