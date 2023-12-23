dwarf_dict = {}


def adding_to_dict(name, colour, physics):
    dwarf_dict[colour] = dwarf_dict.get(colour, {})
    dwarf_dict[colour][name] = dwarf_dict[colour].get(name, physics)
    if dwarf_dict[colour][name] < physics:
        dwarf_dict[colour][name] = physics


while True:
    input_info = input().split(" <:> ")
    if input_info[0] == "Once upon a time":
        break
    else:
        dwarf_name, dwarf_colour, dwarf_physics = input_info[0], input_info[1], int(input_info[2])
        adding_to_dict(dwarf_name, dwarf_colour, dwarf_physics)

sorted_dwarfs = []

for hat in dwarf_dict:
    for name, physic in dwarf_dict[hat].items():
        sorted_dwarfs.append({'length': len(dwarf_dict[hat]), 'name': name, 'physic': physic, 'hat_color': hat})

for show_result in sorted(sorted_dwarfs, key=lambda item: (-item['physic'], -item['length'])):
    print(f"({show_result['hat_color']}) {show_result['name']} <-> {show_result['physic']}")