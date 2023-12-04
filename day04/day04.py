

def parse_file(file):
    parsed_results = {}
    for line in file:
        colon_idx = line.find(":")
        pipe_idx = line.find("|")
        game_num = int(line[0:colon_idx].replace("Card", "").strip())
        winning_numbers = list(map(int, line[colon_idx+1:pipe_idx].split()))
        card_numbers = list(map(int, line[pipe_idx+1:].split()))
        parsed_results[int(game_num)] = {
            "wins" : winning_numbers,
            "card" : card_numbers,
            "cards_won" : 1
        }
    return parsed_results

# PART 1
# As far as the Elf has been able to figure out, you have to figure out which 
# of the numbers you have appear in the list of winning numbers. The first match 
# makes the card worth one point and each match after the first doubles the point 
# value of that card.
# How many points are they worth in total?
def solve_part_day04(game_data):
    total = 0
    cards_won = 0
    is_winning = None
    for game_num, game_results in game_data.items():
        # check for card wins
        matches = 0
        points_won = 0
        for card_num in game_results["card"]:
            if card_num in game_results["wins"]:
                matches += 1
                points_won = 1 if points_won == 0 else points_won * 2
        total += points_won

        # Check if we continue counting card wins
        # This process repeats until none of the copies cause you to win any more cards. 
        # (Cards will never make you copy a card past the end of the table.)
        # if is_winning is None and card_wins == 0: # in case first line has no wins 
        #     is_winning = False
        # elif is_winning is None:
        #     is_winning = True
        # elif cards_won == 0:

        # update card wins 
        cards_won += game_results["cards_won"]
        # update cards gained in later games
        for i in range(1, matches + 1):
            next_game = game_num + i
            # if next_game < len(game_data):
            game_data[next_game]["cards_won"] += (1 * game_results["cards_won"])
    
    # running_total = 0
    # for _, game_results in game_data.items():
    #     running_total += game_results["cards_won"]
    #     print(game_results["cards_won"])
    # print(running_total)

    return total, cards_won

# PART 2
# you win copies of the scratchcards below the winning card equal to the number of matches. 
# So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
# 
# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. 
# So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that 
# the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to 
# win any more cards. (Cards will never make you copy a card past the end of the table.)
# 
# Process all of the original and copied scratchcards until no more scratchcards are won. 
# Including the original set of scratchcards, how many total scratchcards do you end up with?


if __name__ == "__main__":
    input_file = "day04/day04.input"
    with open(input_file, 'r') as f:
        inputs = parse_file(f)
    total_points, total_cards_won = solve_part_day04(inputs)
    print("DAY 4 (part 1): %d" % (total_points))
    print("DAY 4 (part 2): %d" % (total_cards_won))
