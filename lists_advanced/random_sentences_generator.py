names = ["Ewelina", "Alex", "Yana", "Ivo", "Elena", "Dido"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

import random


def get_random_word(words):
    return random.choice(words)


while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_details = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    input_line = input("Click [ENTER] to generate a new one")
    if input_line == "":
        continue
    else:
        break