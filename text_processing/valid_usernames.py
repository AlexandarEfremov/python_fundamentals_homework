# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on
# separate lines.
# A valid username:
#  has length between 3 and 16 characters inclusive
#  can contain only letters, numbers, hyphens, and underscores
#  has no redundant symbols before, after, or in between

valid_usernames = []
username_inputs = input().split(", ")
for name in username_inputs:
    if 3 <= len(name) <= 16:
        if name.isalnum() or "-" in name or "_" in name:
            if " " not in name:
                valid_usernames.append(name)

print("\n".join(valid_usernames))
