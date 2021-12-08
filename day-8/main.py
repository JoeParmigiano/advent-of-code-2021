from display import *

input_filename = "day-8/input.txt"

# Load data into an array
file = open(input_filename, "r")
data = [x.split(' | ') for x in file.read().split('\n')]
for entry in data:
    entry[0] = entry[0].split(' ')
    entry[1] = entry[1].split(' ')

values = []
for entry in data:
    patterns, numbers = entry[0], entry[1]
    mapping = find_wiring_map(patterns)
    value = ''
    for number in numbers:
        segments = wires_to_segments(number, mapping)
        value += segments_to_number(segments)
    values.append(value)

# At this point all the values are known because I didn't read the full task and solved the whole problem unnecessarily
# Now all the questions are trivial...

# Part 1 ----------------------------------------------------------------------
# Number of 1, 4, 7 or 8
count_1478 = 0
for value in values:
    count_1478 += value.count('1') + value.count('4') + value.count('7') + value.count('8')

print(f"Appearances of the digits 1, 4, 7 and 8: {count_1478}.")

# Part 2 ----------------------------------------------------------------------
print(f"Sum of all output values: {sum([int(value) for value in values])}.")