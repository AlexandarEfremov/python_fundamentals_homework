# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a sorted
# list of numbers in ascending order. Use sorted().

string_numbers = input().split()
integer_numbers = []
for digi in string_numbers:
    integer_numbers.append(int(digi))

sorted_numbers = sorted(integer_numbers)
print(sorted_numbers)
