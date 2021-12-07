class Board():
    def __init__(self, matrix):
        self.matrix = matrix
        self.cols = len(matrix)
        self.rows = len(matrix[0])
        self.last = None
        self.matches = []
        for i in range(self.rows):
            self.matches.append([False] *  self.cols)

    def is_winner(self):
        for row in self.matches:
            if all(row):
                return True
        for j in range(self.cols):
            col = [self.matches[i][j] for i in range(self.rows)]
            if all(col):
                return True
        return False

    def add_number(self, number):
        for i in range(self.rows):
            for j in range(self.cols):
                if number == self.matrix[i][j]:
                    self.matches[i][j] = True
        self.last = number

    def score(self):
        sum_unmarked = 0
        for i in range(self.rows):
            for j in range(self.cols):
                sum_unmarked += self.matrix[i][j] * int(not self.matches[i][j])
        return sum_unmarked * self.last

    def __str__(self):
        string = ""
        for i in range(self.rows):
            row_val = ""
            row_mat = ""
            for j in range(self.cols):
                val = (" " + str(self.matrix[i][j]))[-2:]
                mat = "x " if self.matches[i][j] else "  "
                row_val += val + " "
                row_mat += mat + " "
            row = row_val + " |  " +  row_mat
            string += row + "\n"
        return string