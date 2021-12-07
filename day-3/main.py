input_filename = "day-3/input.txt"

# Load data into an array
file = open(input_filename, "r")
data = file.read().split('\n')

# Get info about the data:
bitstring_length = len(data[0])
bitstring_count = len(data)

# Get the most frequent bit
def most_frequent_bit(bitstrings):
    # Count number of 1s on each position
    ones_count = [0] * bitstring_length
    for bitstring in bitstrings:
        for i, bit in enumerate(bitstring):
            ones_count[i] += int(bit)
    # 1 is the most frequent if its count is greater than len(bitstrings) / 2
    mfb = [0] * bitstring_length
    for i, bit in enumerate(ones_count):
        mfb[i] = int(bit >= (len(bitstrings)/2))
    return mfb

gamma_b = most_frequent_bit(data)

# Convert gamma_b to decimal and get gamma
def bin_array_to_dec(bin_array):
    decimal = 0
    for i, bit in enumerate(bin_array):
        decimal += int(bit) * 2**(len(bin_array) - i - 1)
    return decimal

gamma = bin_array_to_dec(gamma_b)

# Epsilon is the complementary of gamma
epsilon = 2**bitstring_length - gamma - 1

# Calculate the power
power = epsilon * gamma
print(f"Power: {power}")

# Part 2 ----------------------------------------------------------------------
# Find oxygen generator rating (ogr)
ogr_candidates = data
ogr_b = None
for step in range(bitstring_length):
    mfb = most_frequent_bit(ogr_candidates)
    ogr_candidates = [bitstring for bitstring in ogr_candidates if (int(bitstring[step]) == mfb[step])]
    if len(ogr_candidates) == 1:
        ogr_b = ogr_candidates[0]
        break

ogr = bin_array_to_dec(ogr_b)
print(f"Oxygen Generator Rating: {ogr}")

# For the CO2 scrubber ratin (csr) do the same but with the less frequent bit
csr_candidates = data
csr_b = None
for step in range(bitstring_length):
    lfb = [(1 - x) for x in most_frequent_bit(csr_candidates)]
    csr_candidates = [bitstring for bitstring in csr_candidates if (int(bitstring[step]) == lfb[step])]
    if len(csr_candidates) == 1:
        csr_b = csr_candidates[0]
        break

csr = bin_array_to_dec(csr_b)
print(f"CO2 Scrubber Rating: {csr}")

# Find the Life Support Rating (lsr)
lsr = ogr * csr
print(f"Life Support Rating: {lsr}")