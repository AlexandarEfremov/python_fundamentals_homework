# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

first_letter = input()
second_letter = input()


def ascii_conversion(a, b):
    a = ord(a)
    b = ord(b)
    char_list = []
    for number in range(a + 1, b):
        new_char = chr(number)
        char_list.append(new_char)
    return char_list

print(" ".join(ascii_conversion(first_letter, second_letter)))
