key = [int(num) for num in input().split()]


def decryption(string_index, string_char):
    key_index = string_index % len(key)
    decrypted_char = ord(string_char) - key[key_index]
    return chr(decrypted_char)


def metal_type(message):
    start_end_index = [index for index, char in enumerate(message) if char == "&"]
    metal = message[start_end_index[0] + 1:start_end_index[1]]
    return metal


def find_location(message):
    start_index = [index for index, char in enumerate(message) if char == "<"]
    end_index = [index for index, char in enumerate(message) if char == ">"]

    location = message[start_index[0] + 1:end_index[0]]
    return location


decrypted_message = []

while True:
    decrypted_message_zero = ''
    input_string = input()
    if input_string == "find":
        break
    for index, char in enumerate(input_string):
        if len(input_string) >= 4:
            decrypted_letter = decryption(index, char)
            decrypted_message_zero += decrypted_letter
    decrypted_message.append(decrypted_message_zero)

for message in decrypted_message:
    print(f"Found {metal_type(message)} at {find_location(message)}")


