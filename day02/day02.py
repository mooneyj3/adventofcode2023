

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

# Part 2
# The power of a set of cubes is equal to the numbers of red, green, and blue 
# cubes multiplied together. For each game, find the minimum set of cubes that 
# must have been present. 
# What is the sum of the power of these sets?
def solve_part_2(file):
    total = 0
    for l in file:
        game_num, line = parse_game_line(l)
        values = {
            "blue" : 0,
            "red" : 0, 
            "green" : 0
        }
        for result in line:
            for colors in result:
                col_cnt = colors.split(" ")
                if int(col_cnt[0]) > values[col_cnt[1]]:
                    values[col_cnt[1]] = int(col_cnt[0])
        # print(line)
        # [['5 green', '8 blue'], ['3 blue', '4 red', '16 green'], ['1 green', '5 red', '6 blue']]
        total += values["blue"] * values["red"] * values["green"]
    return total

if __name__ == "__main__":
    input_file = "day02/day02.input"
    with open(input_file, 'r') as f:
        result = solve_part_1(f)
        print("DAY 2 (part 1): %d" % (result))
    with open(input_file, 'r') as f:
        result = solve_part_2(f)
        print("DAY 2 (part 2): %d" % (result))