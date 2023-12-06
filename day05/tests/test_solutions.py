import unittest
from soilent_green import parse_input_data, get_lowest_location_number
# from day05.soilent_green.soilent_green_is_elves import parse_input_data, get_lowest_location_number

class test_part_1(unittest.TestCase):
    example = """
        seeds: 79 14 55 13
        
        seed-to-soil map:
        50 98 2
        52 50 48
        
        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15
        
        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4
        
        water-to-light map:
        88 18 7
        18 25 70
        
        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13
        
        temperature-to-humidity map:
        0 69 1
        1 0 69
        
        humidity-to-location map:
        60 56 37
        56 93 4
    """

    def test_part_1_solution(self):
        part_1_example_solution = 35
        almanac = parse_input_data(self.example)
        print(almanac)
        part_1_answer = get_lowest_location_number(almanac)
        print("expected solution: " + str(part_1_answer))
        self.assertEqual(part_1_example_solution, part_1_answer)


if __name__ == '__main__':
    unittest.main()