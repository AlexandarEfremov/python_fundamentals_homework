# Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on
# the console

def area(width, height):
    return width * height


width = int(input())
height = int(input())
result = area(width, height)
print(result)