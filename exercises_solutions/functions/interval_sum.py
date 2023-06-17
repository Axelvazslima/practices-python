def soma_intervalo(a, b):
    if a == b:
        return a
    summ = a
    i = a
    while True:
        i += 1
        summ += i
        if i == b: return summ


