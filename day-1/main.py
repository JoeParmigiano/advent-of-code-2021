input_filename = "day-1/input.txt"

# Load data into an array
file = open(input_filename, "r")
data = [int(x) for x in file.read().split('\n')]

def count_depth_increments(depths, window_width):
    increments = 0
    for i in range(len(depths) - window_width):
        window_depth_current = sum(depths[i:i+window_width])
        window_depth_next = sum(depths[i+1:window_width+i+1])
        increments += int(window_depth_next > window_depth_current)
    return increments

print(f"Answer part 1: {count_depth_increments(data, 1)}")
print(f"Answer part 2: {count_depth_increments(data, 3)}")