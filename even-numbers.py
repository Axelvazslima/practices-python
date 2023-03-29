# Printing the even numbers in a range defined by the user

def evenNumbersX():
    print("We give you the even numbers in your desired range")
    wantedNumber = int(input("Range:"))
    for i in range(wantedNumber + 1):
        if i % 2 == 0:
            print(f"{i}")

evenNumbersX()