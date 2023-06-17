def inverte_subseq(seq, ini, count):
    returned_seq = []
    for idx in range(ini, ini + count):
        returned_seq.append(seq[idx])

    for i in range(ini, ini + count):
        for j in range(i + 1, ini + count):
            seq[i], seq[j] = seq[j], seq[i]
    return returned_seq


