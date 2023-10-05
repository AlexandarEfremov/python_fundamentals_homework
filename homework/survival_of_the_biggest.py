# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n
# represents the count of numbers to remove from the list. You should remove the smallest ones, and then, you
# should print all the numbers that are left in the list, separated by a comma and a space ", ".


integer_list = input().split(" ")
digits_list = []
numbers_to_be_removed = int(input())

current_num = 0

for number in integer_list:
    digits_list.append(int(number))

sorted_list = sorted(digits_list)
counter = 0
for digit in sorted_list:
    if counter == numbers_to_be_removed:
        break
    if digit in digits_list:
        digits_list.remove(digit)
        counter += 1

string_list = []
for i in digits_list:
    string_list.append(str(i))
whole_string = ", ".join(string_list)
print(whole_string)
