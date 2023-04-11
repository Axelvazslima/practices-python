# Calculating a Area

def circleArea():
    print("Give me a circle radius and receive it's area back!")
    n = 3.14159
    R = round(float(input("Radius: ")), 2)
    A = n * R**2
    print(f"A={A:.2f}")

circleArea()