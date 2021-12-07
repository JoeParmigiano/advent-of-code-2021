from pandas import DataFrame

input_filename = "day-5/input.txt"

# Load data into an array
file = open(input_filename, "r")
data = file.read().split('\n')

# Convert each line to [[x1, y1], [x2, y2]]
lines = []
for line_raw in data:
    line = line_raw.split(' -> ')
    line[0] = [int(x) for x in line[0].split(',')]
    line[1] = [int(x) for x in line[1].split(',')]
    lines.append(line)

# Determine if a line is horizontal or vertical, to ignore if required
def is_hv(line):
    is_horizontal = (line[0][0] == line[1][0])
    is_vertical   = (line[0][1] == line[1][1])
    return (is_horizontal or is_vertical)

# Initialize grid
rows, cols = 0, 0
for line in lines:
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    rows = (x1 if x1 > rows else rows)
    rows = (x2 if x2 > rows else rows)
    cols = (y1 if y1 > cols else cols)
    cols = (y2 if y2 > cols else cols)

rows += 1
cols += 1

grid = []
for _ in range(rows):
    grid.append([0] * cols)

# Add coverage to each point
def sign(x):
    return 1 if x >= 0 else -1

for line in lines:
    if is_hv(line):
        x0, y0 = line[0][0], line[0][1]
        dx, dy = [line[1][0] - line[0][0], line[1][1] - line[0][1]]
        grid[y0][x0] += 1
        for i in range(sign(dx), dx + sign(dx), sign(dx)):
            grid[y0][x0 + i] += 1
        for j in range(sign(dy), dy + sign(dy), sign(dy)):
            grid[y0 + j][x0] += 1

# Count overlaps
overlaps = 0
for row in grid:
    for cov in row:
        overlaps += int(cov >= 2)

print(f"Number of overlaps: {overlaps}")