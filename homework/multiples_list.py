# Write a program that receives two numbers (factor and count). It should create a list with a length of the given
# count that contains only integer numbers, which are multiples of the given factor. The numbers should be only
# positive, and they should be arranged in ascending order, starting from the value of the factor.

factor_num = int(input())
count_num = int(input())

my_list = []
counter = 0
for _ in range(count_num):
    my_list.append(factor_num + counter)
    counter += factor_num
print(my_list)

