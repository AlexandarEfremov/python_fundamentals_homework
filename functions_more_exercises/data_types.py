# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real",
# or "string".
#  If the data type is an int, multiply the number by 2.
#  If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
#  If the data type is a string, surround the input with "$"


input_type = input()
input_value = input()


def int_multiplication(num):
    number_as_int = int(num)
    return number_as_int * 2


def real_multiplication(num):
    number_as_float = float(num)
    new_number = number_as_float * 1.5
    return f"{new_number:.2f}"


def string_surrounding(string):
    new_string = f"${string}$"
    return new_string


if input_type == "int":
    print(int_multiplication(input_value))
elif input_type == "real":
    print(real_multiplication(input_value))
elif input_type == "string":
    print(string_surrounding(input_value))
