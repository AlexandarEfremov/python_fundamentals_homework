number_of_pieces = int(input())
piano_dict = {}

for i in range(number_of_pieces):
    piece_info = input().split("|")
    piece, composer, key = piece_info[0], piece_info[1], piece_info[2]
    if piece not in piano_dict:
        piano_dict[piece] = {"composer": composer, "key": key}

while True:
    piece_info = input()
    if piece_info == "Stop":
        break
    piece_info = piece_info.split("|")

    if piece_info[0] == "Add":
        piece, composer, key = piece_info[1], piece_info[2], piece_info[3]
        if piece not in piano_dict:
            piano_dict[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif piece_info[0] == "Remove":
        piece = piece_info[1]
        if piece in piano_dict:
            del piano_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif piece_info[0] == "ChangeKey":
        piece, key = piece_info[1], piece_info[2]
        if piece in piano_dict:
            print(f"Changed the key of {piece} to {key}!")
            piano_dict[piece]["key"] = key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in piano_dict.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")