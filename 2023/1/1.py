import re

def sum_first_last_numbers(input):
    """Given list of strings, find the first and last number within each string.
    Concatenate them, add them all together, and return total."""
    # re.search finds first matching regex value in item.
    # .group extracts the matching value from the re.Match object
    get_first_num = [re.search(r'\d', i).group() for i in input]
    # Reversing string with [::-1] to get last number
    get_last_num = [re.search(r'\d', i[::-1]).group() for i in input]

    # Concatenate numbers and convert to integer
    output = [int(first + last) for (first,last) in zip(get_first_num, get_last_num)]

    # Print total of all numbers
    print(sum(output))


# Read in input to a list
input = open("input.txt", "r").read().splitlines()

# Part 1
# Calculate sum for part 1
sum_first_last_numbers(input)


# Part 2
# Convert all spelled out numbers to integer characters
input = ['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen']

input[0]
re.sub("two", "2", input[0])

# This doesn't work because need to replace numbers from left to right only as
# we see them.
input_2 = [i
    .replace("one", "1")
    .replace("two", "2")
    .replace("three", "3")
    .replace("four", "4")
    .replace("five", "5")
    .replace("six", "6")
    .replace("seven", "7")
    .replace("eight", "8")
    .replace("nine", "9")

    for i in input
]

input
input_2

# 29, 83, 13, 24, 42, 14, and 76

# re.search finds first matching regex value in item.
# .group extracts the matching value from the re.Match object
get_first_num = [re.search(r'\d', i).group() for i in input]
# Reversing string with [::-1] to get last number
get_last_num = [re.search(r'\d', i[::-1]).group() for i in input]

# Concatenate numbers and convert to integer
output = [int(first + last) for (first,last) in zip(get_first_num, get_last_num)]
output




# Calculate sum for part 2
sum_first_last_numbers(input_2)
