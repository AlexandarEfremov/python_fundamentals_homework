import re

initial_string = input()
search_pattern = r"(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
results = re.findall(search_pattern, initial_string)
extended_pattern = re.findall(search_pattern, initial_string, flags=re.IGNORECASE)

working_string = results
mirror_words = {}
all_matches = []
for item in working_string:
    working_item = item[1]
    reversed_item = item[3]
    if working_item == reversed_item[::-1]:
        if working_item not in mirror_words and reversed_item not in mirror_words:
            mirror_words[working_item] = reversed_item
        else:
            continue
    if item in extended_pattern:
        working_item = item[1]
        if working_item not in all_matches and working_item not in mirror_words:
            all_matches.append(working_item)

if len(mirror_words) == 0 and len(all_matches) == 0:
    print("No word pairs found!")
    print("No mirror words!")
elif len(mirror_words) > 0 or len(all_matches) > 0:
    total_len = len(mirror_words) + len(all_matches)
    print(f"{total_len} word pairs found!")
    if len(mirror_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        last_key = list(mirror_words.keys())[-1]
        for key, value in mirror_words.items():
            print(f"{key} <=> {value}", end=", " if key != last_key else "\n")

