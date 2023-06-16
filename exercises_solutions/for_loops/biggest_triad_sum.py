seq = input().split()

for i in range(len(seq)):
    seq[i] = int(seq[i])

b_sum = seq[0] + seq[1] + seq[2]

for j in range(len(seq) - 2):
    cur_sum = seq[j] + seq[j +1] + seq[j + 2]
    if cur_sum >= b_sum:
        b_sum = cur_sum
        position = f'tríade: posições {j}, {j +1} e {j + 2}'

print(f"""maior soma: {b_sum}
{position}""")
