def caractere_ausente(seq1, seq2):
    if len(seq1) > len(seq2):
        seq1, seq2 = seq2, seq1
    for i in range(len(seq2)):
        counter = 0
        for j in range(len(seq1)):
            if seq1[j].lower() != seq2[i].lower():
                counter += 1
            if counter == len(seq1):
                return seq2[i].lower()
    if len(seq1) < 1:
        return seq2[0].lower()


