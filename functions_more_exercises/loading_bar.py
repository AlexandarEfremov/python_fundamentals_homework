# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20,
# 30...). Your task is to create a function that returns a loading bar depending on the number you have received in the
# input. Print the result on the console. For more clarification, see the examples below.

number_input = int(input())


def loading_bar(num):
    number_as_single_digit = int(num / 10)
    percentage_bar = ("%" * number_as_single_digit)
    rest_bar = ("." * (10 - number_as_single_digit))
    if 0 <= num <= 90:
        print(f"{num}% [{percentage_bar}{rest_bar}]")
        print("Still loading...")
    elif num == 100:
        print(f"{num}% Complete!")
        print(f"[{percentage_bar}]")


loading_bar(number_input)

