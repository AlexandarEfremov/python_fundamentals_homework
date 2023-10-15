# Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of
# all even numbers.



numbers_list = input().split(", ")

str_indices = map(lambda x: x if int(numbers_list[x]) % 2 == 0 else "no", range(len(numbers_list)))
even_indices = list(filter(lambda a: a != "no", str_indices))
print(even_indices)


