# Write a program that receives a single string. On the first line, print all the digits found in the string, on the second –
# all the letters, and on the third – all the other characters. There will always be at least one digit, one letter, and one
# other character.

string_input = input()
digit = [i for i in string_input if i.isdigit()]
alpha = [i for i in string_input if i.isalpha()]
other = [i for i in string_input if not i.isalpha()]
other_one = [i for i in other if not i.isdigit()]

print("".join(digit))
print("".join(alpha))
print("".join(other_one))

