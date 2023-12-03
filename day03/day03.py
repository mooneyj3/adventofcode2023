
def file_to_2d_list(f):
    input = []
    for l in f:
        input.append(list(l.strip()))
    return input

def is_symbol(ch):
    if ch == ".":
        return False
    if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
        return False
    return True

def is_number(ch):
    return (ord(ch) >= ord('0') and ord(ch) <= ord('9'))


# PART 1
# The engine schematic (your puzzle input) consists of a visual representation 
# of the engine. There are lots of numbers and symbols you don't really understand, 
# but apparently any number adjacent to a symbol, even diagonally, is a "part number" 
# and should be included in your sum. (Periods (.) do not count as a symbol.)
def solve_part_1(input):
    # ord('a')
    # chr(97)
    # . = 46
    # 48 - 57 = 0 - 9
    height = len(input)
    width = len(input[0])

    curr_num = ""
    total = 0
    is_valid_num = False

    for row in range(height):
        for col in range(width):
            curr_char = input[row][col]

            # We are in a number sequence
            if is_valid_num:
                if (is_symbol(curr_char) or curr_char == "."):
                    total += int(curr_num)
                    curr_num = ""
                    is_valid_num = False
                    continue
                elif  col+1 == width and is_number(curr_char):
                    curr_num += curr_char
                    total += int(curr_num)
                    curr_num = ""
                    is_valid_num = False
                    continue
                else:
                    curr_num += curr_char
                    continue
            
            # continue if we are not in a number sequence
            if curr_char == "." or is_symbol(curr_char):
                curr_num = ""
                is_valid_num = False
                continue

            if is_number(curr_char):
                curr_num += curr_char
            
            # check if there it is a valid number
            for r_i in (-1, 0, 1):
                if is_valid_num:
                    break
                for c_i in (-1, 0, 1):
                    if is_valid_num:
                        break
                    if r_i == 0 and c_i == 0:
                        continue
                    if row+r_i < 0 or row+r_i >= height:
                        continue
                    if col+c_i < 0 or col+c_i >= width:
                        continue
                    if is_symbol(input[row+r_i][col+c_i]):
                        is_valid_num = True
            # [row-1][col]
            # [row-1][col+1]
            # [row-1][col-1]
            # [row+1][col]
            # [row+1][col+1]
            # [row+1][col-1]
            # [row][col+1]
            # [row][col-1]



            # if is_symbol(curr_char) or curr_char == '.':


            # # '.'
            # if is_symbol(curr_char) or curr_char == '.':
            #     if curr_num == "":
            #         continue
            #     elif is_valid_num:
            #         total += int(curr_num)
            #         curr_num = ""
            #         is_valid_num = False
            #     else:
            #         continue
            # # is number
            # if ord(curr_char) >= ord('0') and ord(curr_char) <= ord('9'):
            #     curr_num += curr_char
            #     if is_valid_num:
            #         continue
            #     #look for nearby symbol 
            #     if col-1 >= 0 and not is_valid_num:
            #         is_valid_num = is_symbol(input[row][col-1])
            #     if col+1 < width and not is_valid_num:
            #         is_valid_num = is_symbol(input[row][col+1])
            #     if row-1 >= 0 and not is_valid_num:
            #         is_valid_num = is_symbol(input[row-1][col])
            #     if row+1 < height and not is_valid_num:
            #         is_valid_num = is_symbol(input[row+1][col])
            





    return total

# PART 2
def solve_part_2(input):
    return(0)

if __name__ == "__main__":
    input_file = "day03/day03.input"
    with open(input_file, 'r') as f:
        input = file_to_2d_list(f)
    
    result = solve_part_1(input)
    print("DAY 3 (part 1): %d" % (result))

    result = solve_part_2(input)
    print("DAY 3 (part 2): %d" % (result))