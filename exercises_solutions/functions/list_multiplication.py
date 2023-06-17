def multiplica_lista(n, lista):
    new_list = []
    for i in range(len(lista)):
        new_list.append(lista[i])
    if n == 0:
        return []
    for j in range(len(new_list) * (n - 1)):
        new_list.append(new_list[j])
    return new_list


assert multiplica_lista(2, ["Axel", "Mari"]) == ["Axel", "Mari", "Axel", "Mari"]
assert multiplica_lista(0, ["A", 18, 3, 6, 22, 3, "M"]) == []
assert multiplica_lista(0, []) == []
assert multiplica_lista(10, []) == []
assert multiplica_lista(4, ["a"]) == ["a", "a", "a", "a"]

