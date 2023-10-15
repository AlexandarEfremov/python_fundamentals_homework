# Write a program that reads a single string with names separated by comma and space ", ". Sort the names by
# their length in descending order. If 2 or more names have the same length, sort them in ascending order
# (alphabetically). Print the resulting list


def sort_numbers():
    names_list = [name for name in input().split(", ")]
    return sorted(names_list, key=lambda x: (-len(x), x))


print(sort_numbers())

