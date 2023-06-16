palavras = input().split()

for i in range(len(palavras)):
    for j in range(len(palavras[i]) - 1):
        if palavras[i][j].upper() == palavras[i][j + 1].upper():
            print(palavras[i])
            break
