# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a
# given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.


single_number = input()


def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(odd_even_sum(single_number))
