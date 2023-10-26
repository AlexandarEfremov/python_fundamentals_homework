budget = float(input())
number_of_students = int(input())
flour_package_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

from math import ceil

extra_apron_price = single_apron_price * (ceil(number_of_students * 1.2))

free_packages = 0

for student in range(1, number_of_students + 1):
    if student % 5 == 0:
        free_packages += 1

total_price = extra_apron_price + ((single_egg_price * 10) * number_of_students) + \
              (flour_package_price * number_of_students) - (free_packages * flour_package_price)

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    diff = abs(total_price - budget)
    print(f"{diff:.2f}$ more needed.")