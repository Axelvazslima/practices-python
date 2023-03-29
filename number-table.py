# Number table using a for loop

def table():
    tableNumber = float(input(
        "Pick a number and we give you it's multiplication table from 0 to your desired number (stop point): "))
    desiredStop = int(input("Stop point: "))
    for i in range(desiredStop + 1):
        # It can use the result var and eval function as well like a did previously but I wanted this one to be different
        # resultTable = eval(f"{tableNumber * i}")
        # print(f"{tableNumber} * {i} = {resultTable}")
        print(f"{tableNumber} * {i} = {tableNumber * i}")
    print("\n")


table()
