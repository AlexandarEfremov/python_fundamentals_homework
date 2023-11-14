# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string

emoticon_string = input()
emo_index_list = []

for index, char in enumerate(emoticon_string):
    if char == ":":
        print(f"{char}{emoticon_string[index + 1]}")




# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)