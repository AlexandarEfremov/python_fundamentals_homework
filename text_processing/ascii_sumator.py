# Write a program that prints the sum of all found characters between two given characters (their ASCII code). On
# each of the first two lines, you will receive a single character. On the last line, you get a random string. Print the
# sum of the ASCII values of all characters in the random string between the two given characters in the ASCII table.



start_index = ord(input())
end_index = ord(input())

input_string = input()
final_sum = 0

for char in input_string:
    if start_index < ord(char) < end_index:
        final_sum += ord(char)

print(final_sum)

