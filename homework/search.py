# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines,
# you will be given some strings. You should add them to a list and print them. After that, you should filter out only
# the strings that include the given word and print that list too.


n = int(input())
word = input()

string_list = []
filtered_list = []
for _ in range(n):
    word_input = input()
    string_list.append(word_input)

print(string_list)
for elements in string_list:
    if word in elements:
        filtered_list.append(elements)
print(filtered_list)
