number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
from math import ceil

highest_bonus = 0
relative_attendance = 0


def bonus_calculator(attendance, lectures, add_bonus):
    total_bonus = (attendance / lectures) * (5 + add_bonus)
    return total_bonus


for student in range(number_of_students):
    current_attendance = int(input())
    bonus_result = bonus_calculator(current_attendance, total_number_of_lectures, additional_bonus)
    if bonus_result > highest_bonus:
        highest_bonus = bonus_result
        relative_attendance = current_attendance

print(f"Max Bonus: {ceil(highest_bonus)}.")
print(f"The student has attended {relative_attendance} lectures.")
