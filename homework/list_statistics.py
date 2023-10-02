# On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create
# and print two lists:
#  One with all the positives (including 0) numbers
#  One with all the negatives numbers

n = int(input())
positive_list = []
negative_list = []

for _ in range(n):
    num_input = int(input())
    if num_input >= 0:
        positive_list.append(num_input)
    else:
        negative_list.append(num_input)

total_positives = len(positive_list)
sum_negatives = sum(negative_list)

print(positive_list)
print(negative_list)
print(f"Count of positives: {total_positives}")
print(f"Sum of negatives: {sum_negatives}")