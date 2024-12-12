import re

def sum_first_last_numbers_part_1(input):
    """Given list of strings, find the first and last integers within each 
    string. Concatenate them, add them all together, and return total.
    """
    # re.search finds first matching regex value in item
    # .group extracts the matching value from the re.Match object
    get_first_num = [re.search(r'\d', i).group() for i in input]
    # Reversing string with [::-1] to get last number
    get_last_num = [re.search(r'\d', i[::-1]).group() for i in input]

    # Concatenate numbers and convert to integer
    output = [int(first + last) for (first, last) in zip(get_first_num, get_last_num)]

    # Print total of all numbers
    return(sum(output))

def sum_first_last_numbers_part_2(input):
    """Given list of strings, find the first and last numbers (either integers
    or spelled out numbers) within each string. Convert any spelled out numbers
    to integers. Concatenate first and last numbers, add them all together, and 
    return total.
    """
    # re.search finds first matching regex value in item
    # .group extracts the matching value from the re.Match object
    # Adding spelled out numbers (both normal and reversed) to find words
    get_first_num = [re.search(r"[0-9]|one|two|three|four|five|six|seven|eight|nine", i).group() for i in input]
    get_last_num = [re.search(r"[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", i[::-1]).group() for i in input]

    # Create dictionary to convert spelled out numbers to integers
    word_to_int_dict = {
        "one": 1,
        "eno": 1,
        "two": 2,
        "owt": 2,
        "three": 3,
        "eerht": 3,
        "four": 4,
        "ruof": 4,
        "five": 5,
        "evif": 5,
        "six": 6,
        "xis": 6,
        "seven": 7,
        "neves": 7,
        "eight": 8,
        "thgie": 8,
        "nine": 9,
        "enin": 9
    }
    
    # Convert spelled out numbers to integers. Convert integer characters to 
    # integer data types.
    get_first_num = [int(i) if i.isdigit() else word_to_int_dict[i] for i in get_first_num]
    get_last_num = [int(i) if i.isdigit() else word_to_int_dict[i] for i in get_last_num]

    output = [int(str(first) + str(last)) for (first, last) in zip(get_first_num, get_last_num)]
    return(sum(output))

# Read in input to a list
input = open("input.txt", "r").read().splitlines()

sum_first_last_numbers_part_1(input)
sum_first_last_numbers_part_2(input)

