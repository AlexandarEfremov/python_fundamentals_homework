employee_one_per_hour = int(input())
employee_two_per_hour = int(input())
employee_three_per_hour = int(input())
student_count = int(input())

total_answered_per_hour = employee_one_per_hour + employee_two_per_hour + employee_three_per_hour

counter = 0
total_hours = 0
while student_count > 0:
    if counter == 3:
        total_hours += 1
        counter = 0
    student_count -= total_answered_per_hour
    counter += 1
    total_hours += 1

print(f"Time needed: {total_hours}h.")


