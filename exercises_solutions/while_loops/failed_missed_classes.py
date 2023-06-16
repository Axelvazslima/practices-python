rep = 0
while True:
    alunos = list(input())

    if alunos[0] == '-':
        break

    count, faltas = 0, 0
    while count < len(alunos):
        if alunos[count] == 'f':
            faltas += 1
        count += 1
    if faltas > 8:
        rep += 1


print(f"{rep} aluno(s) reprovado(s) por falta.")
