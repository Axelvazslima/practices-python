def baskhara():
    print("""Input all 3 values in a single line (like 03 06 22 -> A = 03, B = 06 and C = 22).
This code will provide you the quadratic equation solved using these values.""")
    values = input("Input three values: ").split()
    line = [float(i) for i in values]
    a = line[0]
    b = line[1]
    c = line[2]
    delta = (b**2) - (4*a*c)

    if 2*a == 0 or delta < 0:
        print("Impossivel calcular")
    else:
        xI = (-b + delta**(1/2))/(2*a)
        xII = (-b - delta**(1/2))/(2*a)
        print(f"""R1 = {xI:.5f}
    R2 = {xII:.5f}""")


baskhara()