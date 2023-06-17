def idosos_inicio(fila):
    position = 0
    for i in range(len(fila)):
        if fila[i] >= 60:
            fila[i], fila[position] = fila[position], fila[i]
            position += 1


