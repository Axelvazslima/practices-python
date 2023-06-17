def cod_letra(linha):
    new_linha = ''
    linha = str(linha)
    letras = ['a', 'b', 'e', 'g', 'i', 'l', 's', 'o']
    subs = ['4', '8', '3', '6', '1', '7', '5', '0']
    for i in range(len(linha)):
        for j in range(len(letras)):
            if linha[i].lower() == letras[j]:
                new_linha += subs[j]
                break
            elif linha[i] == subs[j]:
                new_linha += letras[j].upper()
                break
        else:
            if linha[i].islower():
                new_linha += linha[i].upper()
            elif linha[i].isupper():
                new_linha += linha[i].lower()
            else:
                new_linha += linha[i]
    return new_linha


def cod_space(linha):
    new_linha_lista = cod_letra(linha).split()
    new_string = ''
    for j in range(len(new_linha_lista)):
        white = len(new_linha_lista[j]) * '*'
        if j < len(new_linha_lista) - 1:
            new_string += new_linha_lista[j] + white
        else:
            new_string += new_linha_lista[j]
    return new_string


def ofuscador(linha):
    return cod_space(linha)


