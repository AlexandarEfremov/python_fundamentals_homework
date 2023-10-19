# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second
# line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population has
# less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the
# population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution
# possible"

wealths = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())
sum_of_wealth = 0
noEquals = False
for wealth in wealths:
    sum_of_wealth += wealth
if sum_of_wealth < len(wealths) * minimum_wealth:
    print(f"No equal distribution possible")
    noEquals = True
else:
    start_index = 0
    while start_index < len(wealths):
        while wealths[start_index] < minimum_wealth:
            difference = minimum_wealth - wealths[start_index]
            max_wealth = max(wealths)
            if max_wealth >= minimum_wealth + difference:
                wealths[wealths.index(max_wealth)] -= difference
                wealths[start_index] += difference
        start_index += 1
if not noEquals:
    print(wealths)







