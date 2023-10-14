# Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use
# an appropriate name for the function.

def smallest(some_numbers: list):
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())

some_numbers = smallest([first_number, second_number, third_number])

print(some_numbers)

