# On the first line, you will receive a string. On the second line, you will receive a second string. Write a program that
# removes all the occurrences of the first string in the second until there is no match. At the end, print the remaining
# string

string_to_be_removed = input()
new_string = input()

while string_to_be_removed in new_string:
        new_string = new_string.replace(string_to_be_removed, "")

print(new_string)