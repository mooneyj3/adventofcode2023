import re

def extract_first_last(line):
    return int(re.search(r"\d", line).group() + re.search(r"(\d)(?!.*\d)", line).group())

# PART 1
def solve_part_1(f):
    running_total = 0
    for l in f:
        running_total += extract_first_last(l)
    return running_total

# PART 2


if __name__ == "__main__":
    input_file = "day01.input"
    with open(input_file, 'r') as f:
        result = solve_part_1(f)
        print("DAY 1 (part 1): %d" % (result))