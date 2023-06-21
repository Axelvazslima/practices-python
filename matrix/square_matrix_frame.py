# This function gets a square Matrix and returns it's frame given a starting point (line)


def frame(matrix, k):
    frames = []
    end = k * (-1)
    for i in range(k, len(matrix) + end):
        for j in range(k, len(matrix[i]) + end):
            if i == k or i == len(matrix) - 1 - k or j == k or j == len(matrix[i]) - 1 - k:
                frames.append(matrix[i][j])
    return frames


m = [[1, 2, 3, 4   ],
     [5, 6, 7, 8   ],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
print(frame(m, 2))
