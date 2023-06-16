cont = 0
escalas = []

def my_sum(lista):
    summed = 0
    for i in range(len(lista)):
        summed += lista[i]
    return summed

while True:
    ter = float(input())
    escalas.append(ter)
    cont += 1
    avg = my_sum(escalas) / cont
    print(f"m = {ter:.1f} (média = {avg:.1f})")
    if ter > 10:
        print("ALERTA: limite de sismo atingido!")
        print(f"número de medições: {cont}")
        break
