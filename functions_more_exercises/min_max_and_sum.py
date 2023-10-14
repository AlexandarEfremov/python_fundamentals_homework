# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min
# and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
#  On the first line: "The minimum number is {minimum number}"
#  On the second line: "The maximum number is {maximum number}"
#  On the third line: "The sum number is: {sum of all numbers}"

string_numbers = input().split()
integer_numbers = []
for digi in string_numbers:
    integer_numbers.append(int(digi))

maximum_number = max(integer_numbers)
minimum_number = min(integer_numbers)
total_sum = sum(integer_numbers)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {total_sum}")