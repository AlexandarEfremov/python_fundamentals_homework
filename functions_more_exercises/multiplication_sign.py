# You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative,
# positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.


int_one = int(input())
int_two = int(input())
int_three = int(input())


def multi_sign(a, b, c):
    result = None
    if a == 0 or b == 0 or c == 0:
        result = "zero"
    elif a < 0 or b < 0 or c < 0:
        result = "negative"
    if c > 0 and a < 0 and b < 0 or b > 0 and a < 0 and c < 0 or a > 0 and b < 0 and c < 0 or \
       a > 0 and b > 0 and c > 0:
        result = "positive"
    return result


print(multi_sign(int_one, int_two, int_three))