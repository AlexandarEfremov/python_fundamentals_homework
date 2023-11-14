# Write a program that reads the path to a file and subtracts the file name and its extension

file_path = input().split("\\")

last_directory = file_path[-1]
name, extension = last_directory.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")