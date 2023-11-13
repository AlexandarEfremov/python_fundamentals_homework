# Write a program thatreceives a text and a string of banned words, separated by a comma and space ", ". All banned
# words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line

banned_words = input().split(", ")

text = input()

for word in banned_words:
    while word in text:
        new_word = "*" * len(word)
        text = text.replace(word, new_word)

print(text)


# It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client