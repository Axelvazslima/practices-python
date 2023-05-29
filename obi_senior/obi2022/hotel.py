D = int(input())
A = int(input())
N = int(input()) - 1

aumento = D + N * A

if N >= 15:
    aumento = D + 14 * A
price = (31 - N) * aumento

if D in range(1, 1001) and A in range(1, 1001) and N in range(0, 31):
    print(price)

