# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value
# as a list. Use abs()

input_tab = input().split()

absolute_nums = []
for i in input_tab:
    absolute_nums.append(abs(float(i)))
print(absolute_nums)


