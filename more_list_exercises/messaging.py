# On the first line, you will receive a sequence of numbers separated by a single space. On the second line, you will
# receive a string.
# Your task is to write a program that sends a message only using chars from the given string. Each char the program
# adds to the message should be found by its index. The index you are looking for is the sum of a number's digits
# from the first sequence. If the index is greater than the length of the text, continue counting from the beginning
# (so that you always have a valid index). When you find a char, you should add it to the message and remove it from
# the string. It means that for the following index, the text will contain one character less.

numbers_input = input().split(" ")
message = input()
message_as_list = []
encrypted_message = ""
for i in message:
    message_as_list.append(i)

for number in numbers_input:
    current_index = 0
    for digit in number:
        current_digit = int(digit)
        current_index += current_digit
    if current_index > len(message):
        new_index = current_index - len(message)
        chosen_letter = message_as_list[new_index]
        encrypted_message += chosen_letter
        message_as_list.remove(message_as_list[new_index])
    else:
        chosen_letter = message_as_list[current_index]
        encrypted_message += chosen_letter
        message_as_list.remove(message_as_list[current_index])

print(encrypted_message)
# 9992 562 8933
# This is some message for you

