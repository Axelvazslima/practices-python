# Getting the Max value between 3 values

def maxValue():
    print("Give us three numbers and we return you the greatest one.")
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    biggerAb = (a+b+abs(a-b))/2
    greatest = (biggerAb + c + abs(biggerAb - c))/2
    print(f"{greatest} is the greatest.")

maxValue()