# You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from the
# first input line, which are substrings of any string in the second input line.


sequence_one = input().split(", ")
sequence_two = input().split(", ")

sub_strings = []
for first_string in sequence_one:
    for second_string in sequence_two:
        if first_string in second_string:
            sub_strings.append(first_string)
            break

print(sub_strings)
