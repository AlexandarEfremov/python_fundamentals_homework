initial_energy = int(input())
counter = 0
wins = 0
while initial_energy != -1:
    if counter == 3:
        initial_energy += wins
        counter = 0
    command = input()
    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {initial_energy}")
        break
    elif command.isdigit():
        if initial_energy - int(command) < 0:
            print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
            break
        else:
            initial_energy -= int(command)
            counter += 1
            wins += 1

