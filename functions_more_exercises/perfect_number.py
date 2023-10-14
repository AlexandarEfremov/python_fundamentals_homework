# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its
# positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
#  "We have a perfect number!" - if the number is perfect.
#  "It's not so perfect." - if the number is NOT perfect.

number_input = int(input())


def perfect_num(num):
    aliquot_sum = 0
    counter = 1
    while counter < num:
        if num % counter == 0:
            aliquot_sum += counter
        counter += 1

        if aliquot_sum >= num:
            if aliquot_sum == num:
                return "We have a perfect number!"
            else:
                return "It's not so perfect."
        if aliquot_sum < num and counter == num:
            return "It's not so perfect."

print(perfect_num(number_input))
