def row_sums(matrix):
    sum_list = []
    for row in matrix:
        row_sum = 0
        for each in row:
            row_sum += each
        sum_list.append(row_sum)
    return sum_list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(row_sums(matrix))
