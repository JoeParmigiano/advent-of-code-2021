input_filename = "day-6/input.txt"

# Load data into an array
file = open(input_filename, "r")
data = [int (x) for x in file.read().split(',')]

# Part 2 requires a more optimal way of handling the data
# New list format: each number represents the amount of fishes with an amount
# of days left to give birth equal to its index

schedule = [0] * 9
for fish in data:
    schedule[fish] += 1

def evolve(schedule):
    next_step = [0] * 9
    # New fishes
    next_step[8] = schedule[0]
    # Fishes that gave birth have now 6 days left
    next_step[6] += schedule[0]
    # All fishes have a day less to give birth
    for i in range(8):
        next_step[i] += schedule[i+1]
    return next_step

days = 256
for day in range(days):
    schedule = evolve(schedule)

fishes = sum(schedule)
print(f"Fishes after {days} days: {fishes}.")