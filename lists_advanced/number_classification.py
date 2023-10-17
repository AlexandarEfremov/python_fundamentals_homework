# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and
# prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number


numbers_input = [int(digit) for digit in input().split(", ")]
positive = []
negative = []
even = []
odd = []

for i in numbers_input:
    if i >= 0:
        positive.append(i)
    if i < 0:
        negative.append(i)
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

positive_output = ", ".join(map(str, positive))
negative_output = ", ".join(map(str, negative))
even_output = ", ".join(map(str, even))
odd_output = ", ".join(map(str, odd))

print("Positive: " + positive_output)
print("Negative: " + negative_output)
print("Even: " + even_output)
print("Odd: " + odd_output)