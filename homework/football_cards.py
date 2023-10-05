# Most football fans love it for the goals and excitement. Well, this problem does not. You are up to handle the
# referee's little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1
# to 11. Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players
# remaining, the referee stops the game immediately, and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number. e.g., the
# card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space. You should print the
# count of remaining players on each team at the end of the game in the format: "Team A - {players_count};
# Team B - {players_count}". If the referee terminated the game, print an additional line: "Game was
# terminated".
# Note for the random tests: If a player who has already been sent off receives another card - ignore it.

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
terminated_game = False

foul_cards = input().replace("-", "")
foul_cards_list = foul_cards.split()
for card in foul_cards_list:
    letter, digit = card[0], card[1:]
    if letter == "A":
        if int(digit) not in team_a:
            continue
        else:
            team_a.remove(int(digit))
    elif letter == "B":
        if int(digit) not in team_b:
            continue
        else:
            team_b.remove(int(digit))
    if len(team_a) < 7 or len(team_b) < 7:
        terminated_game = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminated_game:
    print("Game was terminated")
