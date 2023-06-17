def bubblesort(dados):
    for i in range(len(dados)):
        for j in range(i + 1, len(dados)):
            if dados[i] > dados[j]:
                dados[i], dados[j] = dados[j], dados[i]


lista = [3, 9, 1, 2]
bubblesort(lista)
print(lista)
