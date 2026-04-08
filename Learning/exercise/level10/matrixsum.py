def row_sums(matrix):
    row_sums = []
    for each in matrix:
        i = 0
        row_sum = 0
        while i < len(each):
            row_sum += each[i]
            i += 1
        row_sums.append(row_sum)
    return row_sums

def col_sums(matrix):
    col_sums = []
    i = 0
    while i < len(matrix[0]):
        col_sum = 0
        for each in matrix:
            col_sum += each[i]
        i += 1
        col_sums.append(col_sum)
    return col_sums

def matrix_total(matrix):
    matrix_total = 0
    for each in col_sums(matrix):
        matrix_total += each
    return matrix_total

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix_total(matrix))