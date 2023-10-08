# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros,
# and moves them to the back without messing up the other elements. Print the resulting integer list.

initial_string = input().split(", ")
zero_counter = 0
int_list = []
while "0" in initial_string:
    initial_string.remove("0")
    zero_counter += 1
while zero_counter != 0:
    initial_string.append("0")
    zero_counter -= 1
for item in initial_string:
    item = int(item)
    int_list.append(item)
print(int_list)