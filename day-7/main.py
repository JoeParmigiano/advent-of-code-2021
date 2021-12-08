input_filename = "day-7/input.txt"

# Load data into an array
file = open(input_filename, "r")
data = [int (x) for x in file.read().split(',')]
data.sort()

optimal_pos = (data[len(data)//2 - 1] + data[len(data)//2])//2
fuels = [abs(pos - optimal_pos) for pos in data]
fuel = sum(fuels)
print(f"Part 1 fuel: {fuel}")

# Part 2 ----------------------------------------------------------------------
def cost(X, pos):
    fuel = 0
    for x in X:
        delta = abs(pos - x)
        fuel += delta * (delta + 1) / 2
    return fuel

fuels = []
for i in range(len(data) - 1):
    pos = (data[i] + data[i+1]) // 2
    fuels.append(cost(data, pos))

print(min(fuels))