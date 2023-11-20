# Write a program that translates messages from Morse code to English (capital letters). Use this page to help you
# (without the numbers). The letters will be separated by a space (' '). Each word is separated by a ' | '.
# Print the found words on one line, separated by a space

morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

words = morse_code_string = input().split("|")
english_message = []

for word in words:
    morse_letters = word.split()
    english_word = "".join(morse_code_dict[letter] for letter in morse_letters if letter in letter in morse_code_dict)
    english_message.append(english_word)

result = " ".join(english_message)
print(result)

# .. | -- .- -.. . | -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .