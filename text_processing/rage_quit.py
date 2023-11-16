# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants
# something truly spectacular. He asks for your help.
# He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N),
# e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console.
# In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format:
# "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol,
# and for each string, there will be a corresponding number. The input will be given on a single line.


input_data = input()
final_string = ""
temp_string = ""
uniq_symb = []


def is_digit(char):
    return char.isdigit()


for i, char in enumerate(input_data):
    if not is_digit(char):
        temp_string += char.upper()
        if char.lower() not in uniq_symb:
            uniq_symb.append(char.lower())
    else:
        # Check for multi-digit numbers
        j = i + 1
        while j < len(input_data) and is_digit(input_data[j]):
            char += input_data[j]
            j += 1

        multi_value = temp_string * int(char)
        temp_string = multi_value
        final_string += temp_string
        temp_string = ""

print(f"Unique symbols used: {len(uniq_symb)}")
print(final_string)
