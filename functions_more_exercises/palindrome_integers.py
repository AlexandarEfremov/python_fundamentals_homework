# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that
# receives a list of positive integers, separated by comma and space ", ". The function should check if each integer is
# a palindrome - True or False. Print the result.

numbers_set = input().split(", ")

for number in numbers_set:
    reversed_number = number[::-1]
    if number == reversed_number:
        print(True)
    else:
        print(False)

