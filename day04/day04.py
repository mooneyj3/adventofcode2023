def parse_input_data(input_data):
    cards_data = {}
    for line in input_data:
        colon_idx = line.find(":")
        pipe_idx = line.find("|")
        game_num = int(line[0:colon_idx].replace("Card", "").strip())
        winning_numbers = list(map(int, line[colon_idx+1:pipe_idx].split()))
        card_numbers = list(map(int, line[pipe_idx+1:].split()))
        cards_data[int(game_num)] = {
            "wins" : winning_numbers,
            "card" : card_numbers,
            "cards_won" : 1
        }
    return cards_data

# PART 1 & PART 2
def solve_day04(game_data):
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

        # update card wins 
        cards_won += game_results["cards_won"]
        # update cards gained in later games
        for i in range(1, matches + 1):
            next_game = game_num + i
            # if next_game < len(game_data):
            game_data[next_game]["cards_won"] += (1 * game_results["cards_won"])

    return total, cards_won

