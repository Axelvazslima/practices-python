def eh_roteiro(iata, voos, roteiro):
    roteiro = roteiro.split('/')
    destinos = 0
    for i in range(len(roteiro) - 1):
        if iata[roteiro[i + 1]] not in voos[iata[roteiro[i]]]:
            return False
    return True


