"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
🎄 Advent of Code 2024: Day 2 🎅🏼
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

# Read in the data, split the numbers, and convert to integers
reports = []
with open('reports.txt', 'r') as file:
    for line in file:
        # This is a list of lists of these integers
        reports.append(list(map(int, line.strip().split())))

def is_report_safe(report):
    # Create function to check if each report's levels are always 
    # increasing/decreasing within the allowed ranges.
    increasing_check = all([1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1)])
    decreasing_check = all([1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1)])
    return increasing_check or decreasing_check

def part_1(reports):
    # Run through each report and check safety
    safety_checks = []
    for report in reports:
        safety_checks.append(is_report_safe(report))

    # Count total number of safe reports
    print("Part 1: There are " + str(sum(safety_checks)) + " safe reports out of 1000! 🦌")

def part_2(reports):
    # Run through each report, try removing each level in the report and check
    # safety. If any of those tries are safe, then the report is safe.
    safety_checks = []
    for report in reports:
        safety_checks.append(any([is_report_safe(report[:i] + report[i+1:]) for i in range(len(report))]))

    # Count total number of safe reports
    print("Part 2: There are " + str(sum(safety_checks)) + " safe reports out of 1000! 🦌")


part_1(reports)
part_2(reports)