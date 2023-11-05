# You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single
# space (the first element is the key, the second – the value, and so on). Create a dictionary with all the keys and
# values and print it on the console

bakery = {}
ingredients = input().split()

for i in range(0, len(ingredients), 2):
    key = ingredients[i]
    value = ingredients[i + 1]
    bakery[key] = int(value)
print(bakery)