# Write a program that prints all elements from a given sequence of words that occur an odd number of times (caseinsensitive) in it.
#  Words are given on a single line, space-separated.
#  Print the result elements in lowercase, in their order of appearance


word_dict = {}
key_list = []
string_input = input().lower().split()

for word in string_input:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

for key, value in word_dict.items():
    if value % 2 != 0:
        key_list.append(key)

print(" ".join(key_list))