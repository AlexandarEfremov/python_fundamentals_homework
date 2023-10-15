# You will receive a number representing the number of wagons a train has. Create a list (train) with the given length
# containing only zeros. Until you receive the command "End", you will receive some of the following commands:
#  "add {people}" – you should add the number of people in the last wagon
#  "insert {index} {people}" - you should add the number of people at the given wagon
#  "leave {index} {people}" - you should remove the number of people from the wagon. There will be
# no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.

train_cars = int(input())

train_list = [0] * train_cars

while True:
    input_command = input().split()
    if input_command[0] == "End":
        print(train_list)
        break
    elif input_command[0] == "add":
        value = int(input_command[1])
        train_list[-1] += value
    elif input_command[0] == "insert":
        index_one = int(input_command[1])
        value_one = int(input_command[2])
        train_list[index_one] += value_one
    elif input_command[0] == "leave":
        index = int(input_command[1])
        value = int(input_command[2])
        train_list[index] -= value



