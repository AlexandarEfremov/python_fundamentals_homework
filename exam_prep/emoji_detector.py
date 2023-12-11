import re
raw_input = input()
pattern = r"((\*\*|::)([A-Z][a-z]{2,})(\2))"
digit_pattern = r"\d"
matches = re.finditer(pattern, raw_input)
all_digits = re.findall(digit_pattern, raw_input)

cool_score = 1
emoji_list = []

for match in matches:
    emoji = match.group(1)
    emoji_list.append(emoji)
for match in all_digits:
    cool_score *= int(match)

print(f"Cool threshold: {cool_score}")
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
for emo in emoji_list:
    temp_count = 0
    for letter in emo:
        if letter == ":" or letter == "*":
            continue
        else:
            ascii_letter = ord(letter)
            temp_count += ascii_letter
    if temp_count >= cool_score:
        print(emo)
    else:
        continue

