# PART 1
def solve_part_1(f):
    running_total = 0
    for l in f:
        # nums = re.search(r"\d+", l)
        running_total += int()
        idx1 = None
        idx2 = None
        l_len = len(l)
        for i in range(l_len):
            if idx1 is None and str.isdigit(l[i]):
                idx1 = l[i]
            if idx2 is None and str.isdigit(l[l_len-i-1]):
                idx2 = l[l_len-i-1]
            if idx1 is not None and idx2 is not None:
                num = int(idx1 + idx2)
                running_total += num
                break
    return running_total


if __name__ == "__main__":
    input_file = "day01.input"
    with open(input_file, 'r') as f:
        result = solve_part_1(f)
        print("DAY 1 (part 1): %d" % (result))