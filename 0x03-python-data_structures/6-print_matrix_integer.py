def print_matrix_integer(matrix=[[0]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                end_char = ' '
            else:
                end_char = ''
            print("{:d}".format(matrix[i][j]), end=end_char)
        print()
