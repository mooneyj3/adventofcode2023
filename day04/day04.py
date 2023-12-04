

def parse_file(file):
    #columns are fixed width
    # game idx 5-7 
    # scratch idx 10:40
    parsed_results = {}
    for line in file:
        game_num = line[5:8].strip()
        list(map(int, "42 0".split()))
        winning_numbers = list(map(int, line[10:40].split()))
        card_numbers = list(map(int, line[42:117].split()))
        parsed_results[game_num] = {
            "wins" : winning_numbers,
            "card" : card_numbers,
            "cards_won" : 0
        }
    return parsed_results

# PART 1
# As far as the Elf has been able to figure out, you have to figure out which 
# of the numbers you have appear in the list of winning numbers. The first match 
# makes the card worth one point and each match after the first doubles the point 
# value of that card.
# How many points are they worth in total?
def solve_part_1(game_data):
    total = 0
    for game_num, game_results in game_data.items():
        points_won = 0
        for card_num in game_results["card"]:
            if card_num in game_results["wins"]:
                if points_won == 0:
                    points_won = 1
                else:
                    points_won *= 2
        total += points_won
    return total

# PART 2
# you win copies of the scratchcards below the winning card equal to the number of matches. 
# So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
# 
# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. 
# So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that 
# the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to 
# win any more cards. (Cards will never make you copy a card past the end of the table.)
def solve_part_2(game_data):

    return 0


if __name__ == "__main__":
    input_file = "day04/day04.input"
    with open(input_file, 'r') as f:
        inputs = parse_file(f)
    result = solve_part_1(inputs)
    print("DAY 4 (part 1): %d" % (result))
