# Using comprehension, write a program that receives some text, separated by space, and take only those words whose
# length is even. Print each word on a new line


string_input = [string for string in input().split(" ") if len(string) % 2 == 0]
print("\n".join(string_input))


