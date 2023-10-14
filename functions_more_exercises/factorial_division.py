# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

num_one = int(input())
num_two = int(input())


def first_factorial(num):
    current_number = num
    total_factorial = 1
    while current_number != 0:
        total_factorial *= current_number
        current_number -= 1
    return total_factorial


def second_factorial(num):
    current_number = num
    total_factorial = 1
    while current_number != 0:
        total_factorial *= current_number
        current_number -= 1
    return total_factorial


division_result = first_factorial(num_one) / second_factorial(num_two)
print(f"{division_result:.2f}")

