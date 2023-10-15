# On the first line, you will receive words separated by a single space. On the second line, you will receive a
# palindrome. First, you should print a list containing all the found palindromes in the sequence. Then, you should
# print the number of occurrences of the given palindrome in the format: "Found palindrome {number}
# times"

strings = input().split()
desired_pali = input()
palindrome_strings = [string for string in strings if string == "".join(reversed(string))]

counter = 0
for i in palindrome_strings:
    if i == desired_pali:
        counter += 1

print(palindrome_strings)
print(f"Found palindrome {counter} times")