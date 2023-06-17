def soma_simetricos(valores):
    j = len(valores) - 1
    new_lista = []
    for i in range(len(valores)):
        if j == i and len(valores) % 2 != 0:
            new_lista.append(valores[i])
            break
        elif j == i or i > j:
            break
        summ = valores[i] + valores[j]
        new_lista.append(summ)
        j -= 1
    return new_lista


