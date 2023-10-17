amount_of_electrons = int(input())
filled_shells = []

for shell in range(1, amount_of_electrons + 1):
    max_electrons_in_current_shell = 2 * (shell ** 2)
    if amount_of_electrons >= max_electrons_in_current_shell:
        amount_of_electrons -= max_electrons_in_current_shell
        filled_shells.append(max_electrons_in_current_shell)
        if amount_of_electrons == 0:
            break
    else:
        filled_shells.append(amount_of_electrons)
        break

print(filled_shells)



