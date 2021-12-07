from board import Board

input_filename = "day-4/input.txt"

# Load data
file = open(input_filename, "r")
data = file.read().split('\n\n')

# Format data
numbers = [int(x) for x in data[0].split(',')]
matrices_raw = data[1:]
matrices = []
for matrix_raw in matrices_raw:
    matrix = []
    rows_raw = matrix_raw.split('\n')
    for row_raw in rows_raw:
        row = [int (x) for x in list(filter(None, row_raw.split(' ')))]
        matrix.append(row)
    matrices.append(matrix)

# Instantiate boards
boards = []
for matrix in matrices:
    boards.append(Board(matrix))

ranking = []
for number in numbers:
    to_remove = []
    print(f"> Number: {number}")
    for board in boards:
        board.add_number(number)
        if board.is_winner():
            ranking.append(board)
            to_remove.append(board)         
    for board in to_remove:
        boards.remove(board)

print(f"Winner score: {ranking[0].score()}")
print(f"Loser score: {ranking[-1].score()}")
