def idosos_inicio(passengers):
    position = 0
    for i in range(len(passengers)):
        if passengers[i] >= 60:
            for j in range(i, position, -1):
                passengers[j], passengers[j - 1] = passengers[j - 1], passengers[j]
            position += 1
    else: return passengers

