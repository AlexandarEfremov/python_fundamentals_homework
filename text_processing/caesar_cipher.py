# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each character
# with the corresponding character three positions forward in the ASCII table. For example, A would be replaced with
# D, B would become E, and so on. Print the encrypted text.

text_input = input()

encrypted_message = ""

for char in text_input:
    three_forward = ord(char) + 3
    new_char = chr(three_forward)
    encrypted_message += new_char

print(encrypted_message)