# Telling if a number is odd or even or null(0) + if it's positive or negative

def tellerEvenOdd():
    print("Give us a number and we tell you if it's even, odd or null and if it's positive, negative or none.")
    N = int(input("Pick a number: "))
    even = []
    if N == 0:
        print("NULL")
    if N > 0:
        for i in range(2, N+1, 2):
            even.append(i)
        if N in even:
            print("EVEN POSITIVE")
        elif N not in even:
            print("ODD POSITIVE")
    elif N < 0:
        if N % 2 == 0:
            for i in range(N, N+2, 2):
                even.append(i)
            if N in even:
                print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    print(even)

tellerEvenOdd()