import re

def extract_first_last(line):
    return int(re.search(r"\d", line).group() + re.search(r"(\d)(?!.*\d)", line).group())

string_to_num = {
    "one"  : "o1ne",
    "two"  : "t2we",
    "three": "th3ree",
    "four" : "fo4ur",
    "five" : "fi5ve",
    "six"  : "s6ix",
    "seven": "se7ven",
    "eight": "ei8ght",
    "nine" : "ni9ne"
}

def string_alpha_to_num(line):
    for key, value in string_to_num.items():
        line = line.replace(key, value)
    return line

# PART 1
def solve_part_1(f):
    running_total = 0
    for l in f:
        running_total += extract_first_last(l)
    return running_total

# PART 2
def solve_part_2(f):
    # The right calibration values for string "eighthree" is 83 and for "sevenine" is 79.
    running_total = 0
    for l in f:
        new_l = string_alpha_to_num(l)
        num = extract_first_last(new_l)
        running_total += num
    return running_total


if __name__ == "__main__":
    input_file = "day01/day01.input"
    with open(input_file, 'r') as f:
        result = solve_part_1(f)
        print("DAY 1 (part 1): %d" % (result))
    with open(input_file, 'r') as f:
        result = solve_part_2(f)
        print("DAY 1 (part 2): %d" % (result))