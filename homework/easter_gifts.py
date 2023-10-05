# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First,
# you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible
# commands:
#  "OutOfStock {gift}"
# o Find the gifts with this name in your collection, if any, and change their values to "None".
#  "Required {gift} {index}"
# o If the index is valid, replace the gift on the given index with the given gift.
#  "JustInCase {gift}"
# o Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the
# following format:
# "{gift1} {gift2} {gift3} … {giftn}"

gifts_input_line = input().split(" ")

while True:
    command_input = input()
    if command_input == "No Money":
        break
    if "OutOfStock" in command_input:
        out_list = command_input.split(" ")
        gift_to_remove = out_list[1]
        while gift_to_remove in gifts_input_line:
            gift_index = gifts_input_line.index(gift_to_remove)
            gifts_input_line[gift_index] = None
    elif "Required" in command_input:
        replace_list = command_input.split(" ")
        new_gift = replace_list[1]
        replace_index = int(replace_list[2])
        if replace_index < len(gifts_input_line):
            gifts_input_line[replace_index] = new_gift
    elif "JustInCase" in command_input:
        replace_list = command_input.split(" ")
        new_gift = replace_list[1]
        gifts_input_line.pop()
        gifts_input_line.append(new_gift)
while None in gifts_input_line:
    gifts_input_line.remove(None)
print(" ".join(gifts_input_line))



