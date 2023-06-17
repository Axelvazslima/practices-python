print('This code outputs the sum of elements in Matrixes in a list. Like, first list of a Matrix + first list of another Matrix = Number in list\n')




class Matrix:
    def __init__(self, matrix_one, matrix_two):
        self.matrix_one = matrix_one
        self.matrix_two = matrix_two


    def sum_of_matrix_list(self):
        matrix_one, matrix_two = self.matrix_one, self.matrix_two
        sum_of_matrix_list = []
        for i in range(len(matrix_one)):
            matrix_sum = 0
            for j in range(len(matrix_two[i])):
                matrix_sum += matrix_one[i][j] + matrix_two[i][j]
            sum_of_matrix_list.append(matrix_sum)
        return sum_of_matrix_list
    


matrix_one = [[1, 2, 3], [11, 2, 5], [1, 3, 6]]
matrix_two = [[2, 1, 1], [1, 0, 1], [10, 3, 7]]
matrixes = Matrix(matrix_one, matrix_two)
print(Matrix.sum_of_matrix_list(matrixes))