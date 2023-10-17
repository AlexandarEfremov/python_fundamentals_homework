# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints
# the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
#  The numbers 2, 8, 4, and 10 fall into the group of 10's.
#  The numbers 13, 19, 14, and 15 fall into the group of 20's

initial_string = [int(digit) for digit in input().split(", ")]
group = 10
current_list = initial_string

while len(current_list) > 0:
    print(f"Group of {group}'s: {[num for num in current_list if num <= group]}")
    current_list = [num for num in initial_string if num > group]
    group += 10


