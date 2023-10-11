def pricing(food, amount):
    if food == "coffee":
        return 1.5 * amount
    elif food == "water":
        return 1.0 * amount
    elif food == "coke":
        return 1.4 * amount
    elif food == "snacks":
        return 2.0 * amount


food = input()
amount = int(input())
result = pricing(food, amount)
print(f"{result:.2f}")