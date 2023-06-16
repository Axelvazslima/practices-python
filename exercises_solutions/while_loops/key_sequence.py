def main():
    key_seq = [int(i) for i in input().split()]
    nums = []
    while True:
        num = int(input())
        nums.append(num)
        boolean_find_key_seq, indexes = find_seq(key_seq, nums)
        if boolean_find_key_seq:
            break
    print(f"soma = {find_sum(nums, key_seq)}\npos_chave = {indexes[0]} .. {indexes[-1]}")


def my_clear(seq):
    for i in range(len(seq) - 1, -1, -1):
        seq.pop()
    return seq


def find_sum(seq, key_seq):
    summed = 0
    for i in range(len(seq) - len(key_seq)):
        summed += seq[i]
    return summed


def find_seq(key_seq, seq):
    j = 0
    indexes = []
    for i in range(len(seq)):
        if seq[i] == key_seq[j]:
            indexes.append(i)
            j += 1
            if j == len(key_seq):
                return True, indexes
        else:
            indexes = my_clear(indexes)
            if seq[i] == key_seq[0]:
                j = 1
                indexes.append(i)
            else:
                j = 0
    return False, indexes

main()

