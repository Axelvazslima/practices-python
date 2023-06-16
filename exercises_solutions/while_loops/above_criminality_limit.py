ssp = float(input())

sums = 0
medias_str = []
while True:
    medias = input().split()

    if medias[0] == 'fim':
        break

    for x in range(len(medias)):
        medias_str.append(medias[x])
        medias[x] = int(medias[x])

    for j in range(len(medias)):
        sums += medias[j]
        
    media = sums / len(medias)

    if (media * 2) <= ssp:
        break
    elif media > ssp:
        print(' '.join(medias_str))
        media, sums = 0, 0
        medias_str.clear()
    elif ssp == 'fim':
        break
    else:
        media, sums = 0, 0
        medias_str.clear()
