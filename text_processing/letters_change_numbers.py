# You receive a string consisting of a number between two letters. For the given string, you should perform different
# mathematical operations to achieve a result:
#  First, if the letter in front of the number is:
# o Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
#  Next, if the letter after the number is:
# o Uppercase: subtract its position from the resulting number (starting from 1)
# o Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings
# keeping track of only the total sum of all results. Once he started to solve this with more strings and bigger
# numbers, it became quite hard to do it only in his mind. He kindly asks you to write a program that
# performs the operations described above and sums the final results of each string.


input_line = input().split()
total_sum = 0


def get_position_in_alphabet(lett):
    if lett.isupper():
        return ord(lett) - ord('A') + 1
    elif lett.islower():
        return ord(lett) - ord('a') + 1


for block in input_line:
    first_letter = block[0]
    number = int(block[1:-1])
    last_letter = block[-1]
    temp_sum = 0
    if first_letter.isupper():
        result = number / get_position_in_alphabet(first_letter)
        temp_sum += result
    else:
        result = number * get_position_in_alphabet(first_letter)
        temp_sum += result

    if last_letter.isupper():
        temp_sum -= get_position_in_alphabet(last_letter)
    else:
        temp_sum += get_position_in_alphabet(last_letter)

    total_sum += temp_sum
print(f"{total_sum:.2f}")


