def destaca_oscilantes(codigos):
    for i in range(len(codigos)):
        oscilante_char = 0
        for j in range(len(codigos[i]) - 1):
            is_oscilante = int(codigos[i][j]) % 2 == 0 and int(codigos[i][j + 1]) % 2 != 0 or int(codigos[i][j]) % 2 != 0 and int(codigos[i][j + 1]) % 2 == 0
            if is_oscilante:
                oscilante_char += 1
                if oscilante_char == len(codigos[i]) - 1:
                    codigos[i] = '*' + codigos[i]
        if len(codigos[i]) == 1:
                    codigos[i] = '*' + codigos[i]


