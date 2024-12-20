"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
🎄 Advent of Code 2024: Day 3 🎁
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""
import re

# Get just the numbers from each mul(123,123) string, convert them to integers,
# and store in a list.
def extract_numbers(string):
    # Find numbers, convert to integers, return as a list
    return list(map(int, re.findall(r"\d{1,3}", string)))

def part_1(instructions):
    # Find all matching instances of mul(123,123) and put into a list
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", instructions)
    # Extract numbers from mul(123,123)
    get_nums_as_ints = [extract_numbers(i) for i in matches]
    mul_sum_total = sum([i[0] * i[1] for i in get_nums_as_ints])
    print('The answer for Part 1 is ' + str(mul_sum_total) + '🎄.')

def part_2(instructions):
    # Find all mul(123,123) instances, as well as any instances of do() and don't()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", instructions)
    results = []
    # Start with including instances of mul(123,123)
    include_flag = True
    # Loop through each match turning the include_flag on or off with each do
    # or don't. Store extracted, multiplied numbers in final results list.
    for i in matches:
        if i == "do()":
            include_flag = True
        if i == "don't()":
            include_flag = False        
        if include_flag == True and i not in ("do()", "don't"):
            valid_numbers = extract_numbers(i)
            results.append(valid_numbers[0] * valid_numbers[1])

    print('The answer for Part 2 is ' + str(sum(results)) + '🎁.')

# Read in input and run
if __name__ == "__main__":
    # Read in input
    with open('input.txt', 'r') as file:
        instructions = file.read()
    
    part_1(instructions)
    part_2(instructions)