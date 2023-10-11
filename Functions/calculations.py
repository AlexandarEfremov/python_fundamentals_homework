# Create a function that receives three parameters, calculates a result depending on the given operator, and returns
# it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one
# of the following: "multiply", "divide", "add", "subtract".

operator_type = input()
numb_1 = int(input())
numb_2 = int(input())


def calculator(operator_type, number_1, number_2):
    if operator_type == "multiply":
        return number_1 * number_2
    elif operator_type == "divide":
        return int(number_1 / number_2)
    elif operator_type == "add":
        return number_1 + number_2
    elif operator_type == "subtract":
        return number_1 - number_2


print(calculator(operator_type, numb_1, numb_2))
