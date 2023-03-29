def positiveNumbersPrinter():
    print("Write us 6 numbers and we will tell you how many of them are positives")
    everyN = [float(input("Enter 6 numbers (1 at a time): ")),
              float(input()),
              float(input()),
              float(input()),
              float(input()),
              float(input())]
    positives = []
    for i in everyN:
        if i > 0:
            positives.append(i)
    print(f"{len(positives)} positive values")

positiveNumbersPrinter()