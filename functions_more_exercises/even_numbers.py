# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list of
# only the even numbers. Use filter().

string_of_numbers = input().split()

integer_string = []
for digit in string_of_numbers:
    integer_string.append(int(digit))


def is_even(num):
    return num % 2 == 0


filtered_list = list(filter(is_even, integer_string))
print(filtered_list)

