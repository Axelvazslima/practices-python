

def encontra_menores(num, lista):
    default = -1
    for i in lista:
        if i < num:
            return i
    return default


