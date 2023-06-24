def create_array(N):
    array = []
    for i in range(N):
        array.append(0)
    return array


def find_min_max(seq):
    maxx, minn = 0, 51
    max_in, min_i = 0, 0
    for i in range(len(seq)):
        if seq[i] > maxx:
            maxx = seq[i]
            max_in = i
        if seq[i] < minn:
            minn = seq[i]
            min_in = i
    max_in += 1
    min_in += 1
    return max_in, min_in


def sum_of_values_in_same_index_two_square_matrix_same_size(first_matrix, second_matrix):
    values = create_array(len(first_matrix))
    for i in range(len(first_matrix)):
        for j in range(len(first_matrix[i])):
            values[j] += first_matrix[i][j]
            values[j] += second_matrix[i][j]
    maxx, minn = find_min_max(values)
    return maxx, minn


