def price_calc():
    print(f"This code calculates your purchase total. It receives three values (product code, quantity and price) in the same line separeted by white spaces.\nYou do it twice.")
    x = input().split()
    y = input().split()

    code_x, qtd_x, price_x = int(x[0]), int(x[1]), round(float(x[2]), 2)
    code_y, qtd_y, price_y = int(y[0]), int(y[1]), round(float(y[2]), 2)

    x_total = qtd_x * price_x
    y_total = qtd_y * price_y

    total = x_total + y_total

    return total

print(price_calc())