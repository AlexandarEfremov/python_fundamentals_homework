# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already
# exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number –N. Your program should be able to perform a search of contact
# by name and print its details in the format: "{name} -> {number}". In case the contact isn't found, print:
# "Contact {name} does not exist."

phonebook_dict = {}
required_searches = None
while True:
    input_command = input()
    if "-" not in input_command:
        required_searches = int(input_command)
        break
    name = input_command.split("-")[0]
    number = input_command.split("-")[1]
    phonebook_dict[name] = number

for contact in range(required_searches):
    desired_contact = input()
    if desired_contact in phonebook_dict:
        print(f"{desired_contact} -> {phonebook_dict[desired_contact]}")
    else:
        print(f"Contact {desired_contact} does not exist.")


