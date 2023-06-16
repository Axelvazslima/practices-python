vogais = ['a', 'e', 'i', 'o', 'u']
index = []

i = 0
while True:

    palavra = list(input().lower())

    con = 0
    for k in range(len(palavra)):
        diff = 0
        for j in range(len(vogais)):
            if palavra[k] != vogais[j]:
                diff += 1
            if diff == len(vogais):
                con += 1
    if (len(palavra) / 2) > len(palavra) - con:
        index.append(i + 1)
        break

    i += 1

print(index[0])
