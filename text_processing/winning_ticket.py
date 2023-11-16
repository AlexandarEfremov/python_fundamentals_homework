# You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket
# to see if it has a winning combination of symbols:
#  A valid ticket has exactly 20 characters.
#  A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly
# repeated at least 6 times in both halves of the tickets.
#  In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"


# 100% on judge

def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_half = ticket[:10]
    right_half = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uninterrupted_match_length
            if winning_symbol_repetition in left_half and winning_symbol_repetition in right_half:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))




# NB!!!! Zero tests are correct, however total judge score is 72%

# ticket_string = [' '.join(ticket.split()) for ticket in input().split(",")]
#
#
# def symbol_check(left_string, right_string):
#     ticket = left_string + right_string
#     available_symbols = ['@', '#', '$', '^']
#     temp_count_left = 0
#     current_symbol_left = ''
#     for letter in left_string:
#         if letter in available_symbols:
#             current_symbol_left = letter
#             temp_count_left += 1
#         else:
#             if temp_count_left == 0:
#                 continue
#             else:
#                 break
#
#     temp_count_right = 0
#     current_symbol_right = ''
#     for letter in right_string:
#         if letter in available_symbols:
#             current_symbol_right = letter
#             temp_count_right += 1
#         else:
#             if temp_count_right == 0:
#                 continue
#             else:
#                 break
#
#     if temp_count_left < 6 or temp_count_right < 6:
#         return f'ticket "{ticket}" - no match'
#     if (temp_count_left == 10 or temp_count_right == 10) and (current_symbol_left == current_symbol_right):
#         min_count = min(temp_count_left, temp_count_right)
#         return f'ticket "{ticket}" - {min_count}{current_symbol_left} Jackpot!'
#     if temp_count_left >= 6 and temp_count_right >= 6 and current_symbol_left == current_symbol_right:
#         min_count = min(temp_count_left, temp_count_right)
#         return f'ticket "{ticket}" - {min_count}{current_symbol_left}'
#     else:
#         return f'ticket "{ticket}" - no match'
#
#
# for ticket in ticket_string:
#     if len(ticket) != 20:
#         print("invalid ticket")
#         continue
#     left_half = ticket[:10]
#     right_half = ticket[10:]
#     print(symbol_check(left_half, right_half))

# $$$$$$$$$$$$$$$$$$$$, aabb ,th@@@@@@eemo@@@@@@ey
# validticketnomatch:(,Cas$$$$$$$Ca$$$$$$s$

