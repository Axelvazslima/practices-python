even, odd, positive, negative, zero = 0, 0, 0, 0, 0

size = int(input("How many elements do you want this sequence to have? "))
for i in range(size):
    num = int(input())
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else: zero += 1
    if num % 2 == 0:
        even += 1
    else: odd += 1

print(f"{even} valor(es) par(es)\n{odd} valor(es) impar(es)\n{positive} valor(es) positivo(s)\n{negative} valor(es) negativo(s)\n{zero} zero(s)")
