def sum_odd_nums_xy_not_included():
    X, Y = map(int, input().split())

    if X > Y:
        X, Y = Y, X

    summ = 0
    for i in range(X + 1, Y):
        if i % 2 != 0:
            summ += i

    return summ

