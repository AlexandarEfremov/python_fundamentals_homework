# Create a program that receives two strings on a single line separated by a single space. Then, it prints the sum of
# their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum,
# then continue with the next two characters. If one of the strings is longer than the other, add the remaining
# character codes to the total sum without multiplication.


str_one, str_two = input().split()

total_result = 0

if len(str_one) == len(str_two):
    for i in range(0, len(str_one)):
        multiplied_str = ord(str_one[i]) * ord(str_two[i])
        total_result += multiplied_str
elif len(str_one) > len(str_two):
    counter = 0
    for i in range(0, len(str_two)):
        multiplied_str = ord(str_one[i]) * ord(str_two[i])
        total_result += multiplied_str
        counter += 1
    rest_str = str_one[counter:]
    for i in range(len(rest_str)):
        total_result += ord(rest_str[i])
else:
    counter = 0
    for i in range(0, len(str_one)):
        multiplied_str = ord(str_one[i]) * ord(str_two[i])
        total_result += multiplied_str
        counter += 1
    rest_str = str_two[counter:]
    for i in range(len(rest_str)):
        total_result += ord(rest_str[i])

print(total_result)
