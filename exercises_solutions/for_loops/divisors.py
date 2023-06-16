user_num = int(input())

if user_num > 0:
    for i in range(1, user_num):
        if user_num % i == 0:
            print(i)
