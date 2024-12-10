# Read in the data, split the numbers and convert to integers
reports = []
with open('reports.txt', 'r') as file:
    for line in file:
        # This is a list of lists of these integers
        reports.append(list(map(int, line.strip().split())))

# Create function to check if each reports numbers are always increasing/decreasing
# within the allowed ranges.
def is_report_safe(report):
    # Increasing/decreasing within ranges
    increasing_check = all([1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1)])
    # Decreasing within ranges
    decreasing_check = all([1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1)])
    return increasing_check or decreasing_check

# Run through all reports and check safety
safety_checks = []
for report in reports:
    safety_checks.append(is_report_safe(report))

# Count total number of safe reports
print("There are " + str(sum(safety_checks)) + " safe reports out of 1000! 🦌")
