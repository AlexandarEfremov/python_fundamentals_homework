# On the first line, you will receive a single number n. On the following n lines, you will receive integers. After
# that, you will be given one of the following commands:  even  odd  negative  positive Filter all the numbers
# that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())
all_numbers = []
even = []
odd = []
negative = []
positive = []
for _ in range(n):
    int_input = int(input())
    if int_input % 2 == 0 or int_input == 0:
        even.append(int_input)
    if int_input % 2 != 0:
        odd.append(int_input)
    if int_input < 0:
        negative.append(int_input)
    if int_input >= 0:
        positive.append(int_input)

command_input = input()
if command_input == "even":
    print(even)
elif command_input == "odd":
    print(odd)
elif command_input == "negative":
    print(negative)
elif command_input == "positive":
    print(positive)
