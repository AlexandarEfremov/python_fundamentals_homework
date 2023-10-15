# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. Print the
# new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'

text = "aoueiAOUEI"
input_text = input()

input_list= [num for num in input_text if num not in text]
print("".join(input_list))