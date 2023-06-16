i = 0
summ = 0
while True:
    num = int(input())
    if num < 0 and i == 0:
        avg = 0
        break
    elif num < 0:
        break
    i += 1
    summ += num
    avg = summ / i
    if summ > 500:
        break

print(f'{summ}\n{avg:.2f}\n{i}')
