# Code to convert a mesure from m to cm and mm

def mesuresConverter():
    print("Now, it's time for a mesurement conversion from M to CM and MM.")
    m = float(input("Meters: "))
    resultCM = eval(f"{m * 100}")
    resultMM = eval(f"{m * 1000}")
    print(f"""
{m} meters in CM is {resultCM}.
{m} meters in MM is {resultMM}.
""")

mesuresConverter()