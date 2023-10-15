# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
# "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).

def to_do_list():
    todo_notes = []

    while True:
        note = input()
        if note == "End":
            break

        todo_notes.append(note)

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split("-")[0]))
    return [note.split("-")[1] for note in sorted_notes]


result = to_do_list()
print(result)


