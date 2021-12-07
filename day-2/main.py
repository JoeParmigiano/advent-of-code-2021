input_filename = "day-2/input.txt"

# Load data into an array
file = open(input_filename, "r")
data = [x.split(' ') for x in file.read().split('\n')]

# Sum displacements in xyz coordinates
# +x: right   / -x: left        pos[0]
# +y: up      / -y: down        pos[1]
# +z: forward / -z: backwards   pos[2]
pos = [0, 0, 0]
for instruction in data:
    direction, amount = instruction[0], int(instruction[1])
    if direction == "forward":
        pos[2] += amount
    elif direction == "up":
        pos[1] -= amount
    elif direction == "down":
        pos[1] += amount

coverage = pos[1] * pos[2]

print("Part 1")
print(f"Final position: ({pos[0]}, {pos[1]}, {pos[2]})")
print(f"Answer: {coverage}\n\n")

# Part 2
# Add aim and adapt each case to new instructions
pos = [0, 0, 0]
aim = 0
for instruction in data:
    direction, amount = instruction[0], int(instruction[1])
    if direction == "forward":
        pos[2] += amount
        pos[1] += aim * amount
    elif direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount

coverage = pos[1] * pos[2]

print("Part 2")
print(f"Final position: ({pos[0]}, {pos[1]}, {pos[2]})")
print(f"Answer: {coverage}")