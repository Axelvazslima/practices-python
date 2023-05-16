def oldest_son():
    print("The sum of the sons ages equals the mom's age. The function returns the oldest son's age")
    m = int(input("Mom's age (Must be the oldest one and can't be over 101 and must be over 39): "))
    a = int(input("First son age (Can't be under 1 -> Conditions to both sons): "))
    b = int(input("Second son age (Can't be the same as the first one): "))
    c = m - (a + b)

    mom_cond = m in range(40, 111)
    sons_cond = a in range(1, m) and b in range(1, m) and a != b

    sons = [a, b, c]
    sons.sort()
    older = sons[-1]

    if not mom_cond and not sons_cond:
        return f"Not working, didn't match the specifications."

    return older
