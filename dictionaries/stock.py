# You will be given key-value pairs of products and quantities (on a single line separated by space). On the following
# line, you will be given products to search for. Check for each product. You have 2 possibilities:
#  If you have the product, print "We have {quantity} of {product} left".
#  Otherwise, print "Sorry, we don't have {product}"

product_input = input().split()
food_dict = {}

for i in range(0, len(product_input), 2):
    food = product_input[i]
    value = product_input[i + 1]
    food_dict[food] = int(value)

available_food = input().split()

for item in available_food:
    if item in food_dict.keys():
        print(f"We have {food_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")



