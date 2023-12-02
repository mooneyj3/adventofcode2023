

def parse_game_line(line):
    # Game 1: 1 red, 5 blue, 10 green; 5 green, 6 blue, 12 red; 4 red, 10 blue, 4 green
    line = line.replace("Game ", "").strip()
    game_num_idx = line.index(":")
    game_num = int(line[0:game_num_idx])
    line = line[game_num_idx+2:].replace(", ",",").split("; ")
    line = [i.split(',') for i in line]

    return game_num, line

cubes = {
    "red" : 12, 
    "green" : 13, 
    "blue" : 14
}

# Part 1
# Determine which games would have been possible if the bag had been loaded with 
# only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs 
# of those games?
def solve_part_1(file):
    total = 0

    for l in file:
        game_num, line = parse_game_line(l)
        game_counts = True
        
        for result in line:
            for colors in result:
                col_cnt = colors.split(" ")
                if int(col_cnt[0]) > cubes[col_cnt[1]]:
                    game_counts = False
        if game_counts == True:
            total += game_num
    return total

def solve_part_2(file):
    return 0

if __name__ == "__main__":
    input_file = "day02/day02.input"
    with open(input_file, 'r') as f:
        result = solve_part_1(f)
        print("DAY 1 (part 1): %d" % (result))
    with open(input_file, 'r') as f:
        result = solve_part_2(f)
        print("DAY 1 (part 2): %d" % (result))