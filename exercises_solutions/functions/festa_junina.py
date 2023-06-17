def promocao(menu):
    combos = []
    for i in range(len(menu)):
        for j in range(i, len(menu)):
            combos.append(f'{{{menu[i]}, {menu[j]}}}')
    return combos


