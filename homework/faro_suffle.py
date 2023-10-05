# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still
# on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives
# ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of
# faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.


initial_string = input().split(" ")
half_cards = int(len(initial_string) / 2)
total_shuffles = int(input())


for _ in range(total_shuffles):
    new_list = []
    current_index = 0
    while current_index < half_cards:
        for card in range(current_index, len(initial_string), half_cards):
            new_list.append(initial_string[card])
        current_index += 1
    initial_string = new_list
print(new_list)

