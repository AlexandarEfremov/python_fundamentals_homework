# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use
# round().

def rounded_number(n):
    return round(n)

input_string = input()
new_list = []

for num in input_string.split():
    new_numb = float(num)
    new_list.append(rounded_number(new_numb))
print(new_list)