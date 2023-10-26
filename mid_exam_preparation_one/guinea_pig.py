# On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buysfor a month (30 days).
# On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of
# hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of 1/3 of its
# weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!


food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
guinea_weight = float(input())

for i in range(1, 31):
    eaten_food = 0.3
    food_quantity -= eaten_food
    if i % 2 == 0:
        given_hay = food_quantity * 0.05
        hay_quantity -= given_hay
    if i % 3 == 0:
        cover_amount = guinea_weight / 3
        cover_quantity -= cover_amount

if food_quantity > 0 and hay_quantity > 0 and cover_quantity > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, "
          f"Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
else:
    print("Merry must go to the pet store!")

