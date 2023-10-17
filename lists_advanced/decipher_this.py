# You are given a secret message you should decipher. To do that, you need to know that in each word:
#  the second and the last letter are switched (e.g., Holle means Hello)
#  the first letter is replaced by its character code (e.g., 72 means H)

secret_message = input().split(" ")


def char_extraction(message):
    entire_message = ''
    for word in message:
        digi_str = ''
        rest = ''
        for char in word:
            if char.isdigit():
                digi_str += char
            else:
                rest += char
        str_as_char = chr(int(digi_str))
        together = str_as_char + rest
        if entire_message:
            entire_message += " "
        entire_message += together
    return entire_message


def letter_swap(message):
    message = char_extraction(message)
    total_sentence = ''
    for word in message.split(" "):
        if len(word) <= 2:
            if total_sentence:
                total_sentence += " "
            total_sentence += word
            continue
        swapped_word = word[0] + word[-1] + word[2:-1] + word[1]
        if total_sentence:
            total_sentence += " "
        total_sentence += swapped_word
    return total_sentence


print(letter_swap(secret_message))
