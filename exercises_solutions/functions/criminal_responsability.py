def my_function(string):
    lista = string.split()
    try:
        for index in range(len(lista)):
            lista[index] = int(lista[index])
    except:
        pass
    return lista


def maioridade_penal(pessoas, idades):
    output = ''

    pessoas = my_function(pessoas)
    idades = my_function(idades)
    if len(pessoas) == 0 or len(idades) == 0:
        return output

    maiores = []
    for i in range(len(pessoas)):
        if idades[i] >= 18:
            maiores.append(pessoas[i])

    for j in range(len(maiores)):
        output += maiores[j]
        if j < len(maiores) - 1:
            output += ' '
    return output

