import re

with open('input.txt', 'r') as file:
    instructions = file.read()

# Find all matching instances of mul(123,123) and put into a list
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", instructions)

# Get just the numbers from each mul(123,123), convert them to integers,
# multiply, and sum them.
get_nums_as_ints = [list(map(int, re.findall(r"\d{1,3}", i))) for i in matches]
sum([i[0] * i[1] for i in get_nums_as_ints])
