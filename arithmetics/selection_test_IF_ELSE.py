def selection():
    A, B, C, D = map(int, input().split())

    condition = B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and A % 2 == 0
    
    return condition

