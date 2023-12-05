from day04 import parse_input_data, solve_day04
INPUT_FILE = "day04/day04.input"

def data_to_string_list(input_data: str, is_file: bool = True) -> list[str]:
    lines = None
    if is_file:
        with open(input_data, 'r') as f:
            lines = f.read()
    return [line.strip() for line in lines.split('\n')]

def main():
    input_data = data_to_string_list(INPUT_FILE)
    cards_data = parse_input_data(input_data)
    total_points, total_cards_won = solve_day04(cards_data)
    print("DAY 4 (part 1): %d" % (total_points))
    print("DAY 4 (part 2): %d" % (total_cards_won))


if __name__ == '__main__':
    main()