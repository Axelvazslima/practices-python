def calcula_verificador(cpf):
    mult, total = 2, 0
    for i in range(len(cpf) -1, -1, -1):
        total += int(cpf[i]) * mult
        mult += 1
    calc = (total * 10) % 11
    return '0' if calc == 10 else str(calc)


def calcula_digitos_verificacao(cpf):
    verificador = ''
    verificador += calcula_verificador(cpf)
    cpf += calcula_verificador(cpf)
    return verificador + calcula_verificador(cpf)


print(calcula_digitos_verificacao("153245875"))
