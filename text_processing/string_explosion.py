# Write a program that reads a string from the console that contains:
#  Explosions marked with '>'
#  Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
#  Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark
# ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the
# explosion character – '>'

explosion_string = input()

final_string = ""
strength = 0

for index in range(len(explosion_string)):
    if strength > 0 and explosion_string[index] != ">":
        strength -= 1
    elif explosion_string[index] == ">":
        final_string += explosion_string[index]
        strength += int(explosion_string[index + 1])
    else:
        final_string += explosion_string[index]
print(final_string)
