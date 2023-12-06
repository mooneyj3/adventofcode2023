#!/usr/bin/env python3

from soilent_green import get_lowest_location_number, parse_input_data
INPUT_FILE = "day05.input"

def data_to_string(input_data: str, is_file: bool = True) -> str:
    lines = None
    if is_file:
        with open(input_data, 'r') as f:
            lines = f.read()
    else:
        lines = input_data
    return lines

def main():
    input_data = data_to_string(INPUT_FILE)
    almanac = parse_input_data(input_data)
    lowest_location = get_lowest_location_number(almanac)
    print("DAY 5 (part 1): %d" % (lowest_location))


if __name__ == "__main__":
    main()