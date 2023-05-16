def odd_numbers():
    print("You will input a number (1 <= int <= 1000) and the program will return you a list of all odd numbers before or equal that")
    x = int(input("Input a number: "))

    cond = x in range(1, 1001)
    over = x > 1000
    under = x < 1
    msg = f"Your number doesn't match the conditions for the code to run. You picked {x}."
    if not cond and over:
        return f"{msg} {x} > 1000."
    elif not cond and under:
        return f"{msg} {x} < 1."

    odds = []
    for i in range(x + 1):
        odd = i % 2 != 0
        if odd:
            odds.append(i)
    return odds
