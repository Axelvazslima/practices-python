def fuel_consumption():
    print("This code calculates your gas consumption based on your travelled KM and on your liters of gas.")
    while True:
        try:
            x = int(input("Input your total KM: "))
            y = round(float(input("Input your total gas liters: ")), 1)
            break
        except:
            print(f'Invalid type, try again. First one is an int and the second one is a float.')
            pass
    avg = x / y

    return avg

