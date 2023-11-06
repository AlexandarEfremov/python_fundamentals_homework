# You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line
# on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to
# collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000]


resource_list = []
resource_dict = {}
input_command = input()

while input_command != "stop":
    resource_list.append(input_command)
    input_command = input()

for i in range(0, len(resource_list), 2):
    resource = resource_list[i]
    quantity = int(resource_list[i + 1])
    if resource not in resource_dict:
        resource_dict[resource] = quantity
    else:
        resource_dict[resource] += quantity

for key, value in resource_dict.items():
    print(f"{key} -> {value}")