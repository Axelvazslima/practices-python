irmas = []
for i in range(3):
    n = int(input())
    if n not in range(5, 101):
        break
    irmas.append(n)
else:
    for j in range(len(irmas)):
        for k in range(len(irmas)):
            if irmas[j] > irmas[k]:
                irmas[j] , irmas[k] = irmas[k], irmas[j]
    print(irmas[1])
