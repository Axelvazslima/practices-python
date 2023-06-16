wanted_num = int(input())
int_list = [int(i) for i in input().split()]

if wanted_num in int_list:
    print('sim')

else:
    print('não')
