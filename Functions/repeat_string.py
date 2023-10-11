# Write a function that receives a string and a counter n. The function should return a new string – the result of
# repeating the old string n times. Print the result of the function. Try using lambda.

concat = lambda x, y: x * y

string_input = input()
how_many_times = int(input())
result = concat(string_input, how_many_times)
print(result)