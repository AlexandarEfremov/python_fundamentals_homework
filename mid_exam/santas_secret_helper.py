integer_key = int(input())
import re


def name_decoder(key, name_input):
    temp_name = ''
    for letter in name_input:
        new_letter = chr(ord(letter) - key)
        temp_name += new_letter
    return temp_name


valid_names = []

while True:
    input_info = input()
    if input_info == "end":
        break
    else:
        decrypted_name = name_decoder(integer_key, input_info)
        pattern = r"@([A-Z][a-z]+)[^!@\-:>]+!([G]|[N])!"
        match = re.search(pattern, decrypted_name)
        if match:
            name = match.group(1)
            status = match.group(2)
            if status == "G":
                valid_names.append(name)
            else:
                continue

for name in valid_names:
    print(name)
