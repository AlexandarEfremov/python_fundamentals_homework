password_input = input()


def password_check(password):
    errors = []
    if len(password) < 6 or len(password) > 10:
        errors.append("Password must be between 6 and 10 characters")
    digit_counter = 0
    for letter in password:
        if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90:
            continue
        elif letter.isdigit():
            digit_counter += 1
            continue
        else:
            errors.append("Password must consist only of letters and digits")
            break
    if digit_counter < 2:
        errors.append("Password must have at least 2 digits")
    if errors:
        return "\n".join(errors)
    else:
        return "Password is valid"


print(password_check(password_input))

