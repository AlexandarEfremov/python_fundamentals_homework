# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

input_string = input()
split_string = input_string.split()
reversed_string = []
for num in split_string:
    if int(num) > 0:
        num = int(num) * -1
        reversed_string.append(num)
    elif int(num) < 0:
        num = abs(int(num))
        reversed_string.append(num)
    else:
        num = int(num)
        reversed_string.append(num)
print(reversed_string)
