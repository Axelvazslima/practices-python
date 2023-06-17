print('This code return the sum of each index of two matrixes in another matrix.\nFor example matrix line 1, column 1 + matrix line 1, column 1 = new matrix line 1, column 1.\n')




class Matrix:
    def __init__(self, matrix_one, matrix_two):
        self.matrix_one = matrix_one
        self.matrix_two = matrix_two


    def add_two_matrix(self):
        matrix_one, matrix_two = self.matrix_one, self.matrix_two
        new_matrix = []
        for i in range(len(matrix_one)):
            new_list = []
            for j in range(len(matrix_two[i])):
                matrix_cur = matrix_one[i][j] + matrix_two[i][j]
                new_list.append(matrix_cur)
            new_matrix.append(new_list)
        return new_matrix




matrix_one = [[1, 2, 3], [2, 4, 3], [10, 9, 8]]
matrix_two = [[2, 4, 2], [1, 4, 3], [12, 1, 2]]
matrixes = Matrix(matrix_one, matrix_two)
print(Matrix.add_two_matrix(matrixes))