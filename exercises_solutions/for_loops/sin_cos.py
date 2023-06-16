import math

angulo_in = float(input())
delta = float(input())
linhas = int(input())

print("|Angulo|   Seno|Cosseno|")
for i in range(int(linhas)):
    conta = angulo_in + (delta * i)
    seno = math.sin(math.radians(conta))
    cosseno = math.cos(math.radians(conta))
    print(f"|{' ' * (len('angulo') - len(str(round(conta, 1))))}{conta:.1f}|{seno:.5f}|{cosseno:.5f}|")
