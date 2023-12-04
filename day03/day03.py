
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
    return total

def extract_left_num(row, col, input):
    i = 0
    curr_num = ""
    while is_number(input[row][col+i]):
        curr_num = input[row][col+i] + curr_num
        i -= 1
    return curr_num

def extract_right_num(row, col, input):
    i = 0
    curr_num = ""
    while col+i < len(input) and is_number(input[row][col+i]):
        curr_num += input[row][col+i]
        i += 1
    return curr_num




# PART 2
# The missing part wasn't the only issue - one of the gears in the engine is wrong. 
# A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio 
# is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up so that 
# the engineer can figure out which gear needs to be replaced.
def solve_part_2(input):
    height = len(input)
    width = len(input[0])
    total = 0

    for row in range(height):
        for col in range(width):
            curr_char = input[row][col]
            
            if curr_char != '*':
                continue

            num_holder = []
            curr_num = ""

            # Find the neighboring numbers
            # worried about '.' in row above and below

            # check left
            if is_number(input[row][col-1]):
                num_holder.append(int(extract_left_num(row, col-1, input)))
            
            #check right
            if is_number(input[row][col+1]):
                num_holder.append(int(extract_right_num(row, col+1, input)))
            
            #check above
            if is_number(input[row-1][col]): # center above
                _l_num = ""
                _r_num = ""
                if is_number(input[row-1][col-1]):
                    _l_num = extract_left_num(row-1, col-1, input)
                if is_number(input[row-1][col+1]):
                    _r_num = extract_right_num(row-1, col+1, input)
                num_holder.append(int(_l_num + input[row-1][col] + _r_num))
                # print(_l_num + " " + _r_num)
            else:
                if is_number(input[row-1][col-1]):
                    num_holder.append(int(extract_left_num(row-1, col-1, input)))
                if is_number(input[row-1][col+1]):
                    _r_num = extract_right_num(row-1, col+1, input)
                    num_holder.append(int(_r_num))

            # check below
            if is_number(input[row+1][col]):
                _l_num = ""
                _r_num = ""
                if is_number(input[row+1][col-1]):
                    _l_num = extract_left_num(row+1, col-1, input)
                if is_number(input[row+1][col+1]):
                    _r_num = extract_right_num(row+1, col+1, input)
                num_holder.append(int(_l_num + input[row+1][col] + _r_num))
            else:
                if is_number(input[row+1][col-1]):
                    num_holder.append(int(extract_left_num(row+1, col-1, input)))
                if is_number(input[row+1][col+1]):
                    _r_num = extract_right_num(row+1, col+1, input)
                    num_holder.append(int(_r_num))
            
            
            # check num_holder
            if len(num_holder) != 2:
                continue
            print(num_holder)
            total += num_holder[0] * num_holder[1]





    return total

if __name__ == "__main__":
    input_file = "day03/day03.input"
    with open(input_file, 'r') as f:
        inputs = file_to_2d_list(f)
    
    result = solve_part_1(inputs)
    print("DAY 3 (part 1): %d" % (result))

    result = solve_part_2(inputs)
    print("DAY 3 (part 2): %d" % (result))