


# The almanac (your puzzle input) lists all of the seeds that need to be planted. 
# It also lists what type of soil to use with each kind of seed, what type of fertilizer 
# to use with each kind of soil, what type of water to use with each kind of fertilizer, 
# and so on. Every type of seed, soil, fertilizer and so on is identified with a number, 
# but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't 
# necessarily related to each other.

# The almanac starts by listing which seeds need to be planted

# The rest of the almanac contains a list of maps which describe how to convert numbers 
# from a source category into numbers in a destination category. 
# seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). 
#       This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.
# 
# Each line within a map contains three numbers: 
#        the destination range start, 
#        the source range start, 
#        and the range length.

# Any source numbers that aren't mapped correspond to the same destination number.
#  So, seed number 10 corresponds to soil number 10.

# The gardener and his team want to get started as soon as possible, 
# so they'd like to know the closest location that needs a seed. Using these maps, 
# find the lowest location number that corresponds to any of the initial seeds.

def slice_int_array(int_str: str) -> list[str]:
    return [int(l) for l in int_str.strip().split()]

def parse_input_data(input_data: list[str]) -> dict:
    current_map = None
    almanac = {}
    for line in input_data.split('\n'):
        if line.strip() == '':
            current_map = None
            continue
        elif 'map' in line and current_map is None: 
            # note this doesn't check that the dictionary key disn't already set/exists
            current_map = line[0:line.index(" map")].strip().replace("-to-", "|")
            almanac[current_map] = []
            continue
        elif 'seeds' in line and current_map is None:
            almanac["seeds"] = slice_int_array(line[line.index(':')+1:])
            continue
        else:
           almanac[current_map].append(slice_int_array(line)) 
    return almanac

def get_next_dest_key(almanac: dict, prefix: str) -> str:
    # TODO: create short function to get the next mapping from the dictionary keys
    for key in almanac.keys():
        if key.startswith(prefix):
            return key.split('|')[1]
    return "You done goofed!"

# Each line within a map contains three numbers: 
#        the destination range start, 
#        the source range start, 
#        and the range length.
def get_final_destination(start_num: int, almanac: dict, src_key: str = 'seed', dest_key: str = 'soil') -> int:

    dest_num = start_num
    
    # print(src_key + '|' + dest_key)
    # here we are recursing through the lists
    for m in almanac[src_key + '|' + dest_key]:
        #check if seed is in cource range
        if start_num >= m[1] and start_num < m[1] + m[2]:
            offset = start_num - m[1]
            dest_num = start_num - m[1] + m[0]
            break
    
    # if dest_num is not None:
    #     dest_num = start_num
    # # print(dest_num, end=" ")

    if dest_key == 'location':
        return dest_num
    
    next_dest_key = get_next_dest_key(almanac, dest_key)
    
    return get_final_destination(dest_num, almanac, dest_key, next_dest_key)

# PART 1
def get_lowest_location_number(almanac: dict) -> int:
    
    seeds = almanac.pop('seeds')
    final_locs = []
    
    # for seed in almanac["seeds"]:
    for seed in seeds:
        # print("SEED [" + str(seed) + "] : ", end='')
        final_locs.append(get_final_destination(seed, almanac))

    # print(final_locs)

    return min(final_locs)
