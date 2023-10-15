happy_string = input().split()
happy_factor = int(input())

happy_int = list(map(lambda x: int(x) * happy_factor, happy_string))
average_happiness = sum(happy_int) / len(happy_int)

happy_employees = list(filter(lambda x: x >= average_happiness, happy_int))
total_employees = len(happy_int)

if len(happy_employees) >= total_employees / 2:
    print(f"Score: {len(happy_employees)}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{total_employees}. Employees are not happy!")
