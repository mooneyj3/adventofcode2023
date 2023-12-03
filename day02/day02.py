def parse_game_line(line):
    # parse out game number
    line = line.replace("Game ", "").strip()
    game_num = int(line[0:line.index(":")])
    
    # parse game results
    line = line[line.index(":")+2:].split("; ")
    game = {"red": [], "blue": [], "green": []}
    for i in range(len(line)):
        result = line[i].split(", ")
        for r in result:
            _r = r.split(" ")
            game[_r[1]].append(int(_r[0]))
    
    return game_num, game

cubes = {
    "red" : 12, 
    "green" : 13, 
    "blue" : 14
}

# Part 1
def solve_part_1(file):
    total = 0
    for l in file:
        game_num, game = parse_game_line(l)
        game_counts = True
        for key, value in game.items():
            if max(game[key]) > cubes[key]:
                game_counts = False
                break
        if game_counts == True:
            total += game_num
    return total

# Part 2
def solve_part_2(file):
    total = 0
    for l in file:
        game_num, game = parse_game_line(l)
        sub_total = 1
        for key in game.keys():
            sub_total *= max(game[key])
        total += sub_total
    return total

if __name__ == "__main__":
    input_file = "day02/day02.input"
    with open(input_file, 'r') as f:
        result = solve_part_1(f)
        print("DAY 2 (part 1): %d" % (result))
    with open(input_file, 'r') as f:
        result = solve_part_2(f)
        print("DAY 2 (part 2): %d" % (result))