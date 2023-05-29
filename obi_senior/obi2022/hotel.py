D = int(input())
A = int(input())
N = int(input()) - 1

aumento = D + N * A

if N >= 15:
    aumento = D + 14 * A
price = (31 - N) * aumento

print(price)
