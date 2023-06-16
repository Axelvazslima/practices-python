size = int(input())

nums = []

for i in range(size):
    num = int(input())
    nums.append(num)

above, below = 0, 0
menor_num, maior_num = nums[0], nums[0]

for i in nums:
    if i < menor_num:
        menor_num = i
    elif i > maior_num:
        maior_num = i
    media = (maior_num + menor_num) / 2

for k in nums:
    if k > media:
        above += 1
    elif k < media:
        below += 1

print(f"""Menor número: {menor_num}
Maior número: {maior_num}
Média dos extremos: {media:.2f}
{below} número(s) abaixo da média
{above} número(s) acima da média""")
