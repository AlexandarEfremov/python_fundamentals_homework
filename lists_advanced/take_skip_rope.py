string_input = input()
digit_list = [int(num) for num in string_input if num.isdigit()]
string_list = [string for string in string_input if not string.isdigit()]
working_list = string_list.copy()

take_list = [digi for index, digi in enumerate(digit_list) if index % 2 == 0]
skip_list = [digi for index, digi in enumerate(digit_list) if index % 2 != 0]

result = []
while take_list or skip_list:
    if take_list:
        m = take_list.pop(0)
        result.extend(working_list[:m])
        working_list = working_list[m:]
    if skip_list:
        n = skip_list.pop(0)
        working_list = working_list[n:]

print("".join(result))
