password = input()

new_pass = password[0] + ''
j = 0
for index in range(1, len(password)):
    i = password[index]
    if i == 'a' or  i == 'A':
        i = '4'
        j += 1
    elif i == 'e' or i == 'E':
        i = '3'
        j += 1
    elif i == 'i' or i == 'I':
        i = '1'
        j += 1
    elif i == 'o' or i == 'O':
        i = '0'
        j += 1
    new_pass = new_pass + i

print(f"{new_pass} ({j} troca(s))")
