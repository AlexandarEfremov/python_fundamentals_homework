first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

if first_line[0] == "1" and second_line[0] == "1" and third_line[0] == "1":
    print("First player won")
elif first_line[0] == "2" and second_line[0] == "2" and third_line[0] == "2":
    print("Second player won")
elif first_line[1] == "1" and second_line[1] == "1" and third_line[1] == "1":
    print("First player won")
elif first_line[1] == "2" and second_line[1] == "2" and third_line[1] == "2":
    print("Second player won")
elif first_line[2] == "1" and second_line[2] == "1" and third_line[2] == "1":
    print("First player won")
elif first_line[2] == "2" and second_line[2] == "2" and third_line[2] == "2":
    print("Second player won")
elif first_line[0] == "1" and first_line[1] == "1" and first_line[2] == "1":
    print("First player won")
elif first_line[0] == "2" and first_line[1] == "2" and first_line[2] == "2":
    print("Second player won")
elif second_line[0] == "1" and second_line[1] == "1" and second_line[2] == "1":
    print("First player won")
elif second_line[0] == "2" and second_line[1] == "2" and second_line[2] == "2":
    print("Second player won")
elif third_line[0] == "1" and third_line[1] == "1" and third_line[2] == "1":
    print("First player won")
elif third_line[0] == "2" and third_line[1] == "2" and third_line[2] == "2":
    print("Second player won")
elif first_line[2] == "1" and second_line[1] == "1" and third_line[0] == "1":
    print("First player won")
elif first_line[2] == "2" and second_line[1] == "2" and third_line[0] == "2":
    print("Second player won")
elif first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1":
    print("First player won")
elif first_line[0] == "2" and second_line[1] == "2" and third_line[2] == "2":
    print("Second player won")
else:
    print("Draw!")