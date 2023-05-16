def various_areas():
    print("Input three values separated by white spaces. Last one is height, the others are the base/sides.\nThey are only used if necessary, if you don't need them in your respective geometric figure to discover it's area, just set it to 0.")
    a, b, c = map(float, input().split())

    pi = 3.14159

    pick_number = int(input("What figure do you want the area of?\nFrom 1 to 5 in order: Triangle, circle, trapeze, square and rectangle: "))

    figures = [(a * c) / 2,
    pi * c ** 2,
    (a + b) * c / 2,
    b ** 2,
    a * b]


    return figures[pick_number - 1]

