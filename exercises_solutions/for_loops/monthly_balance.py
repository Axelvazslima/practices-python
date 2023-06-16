meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

mes = 0
for m in range(12):
    balances = input().split()
    for i in range(len(balances)):
        balances[i] = float(balances[i])
    blc = balances[0] - balances[1]
    output = f'{meses[mes]:<3} {blc:4.1f}'
    print(output)
    mes += 1
    if mes == 12: break
