# Average grades with A's weight = 3.5 and B's weight = 7.5

def avgGradesWeight():
    print("""Your grades must be from 0 to 10.
First grade weights 3.5 and second grade weights 7.5""")
    A = round(float(input("First grade: ")), 1)
    B = round(float(input("Second grade: ")), 1)
    if A <= 10 and B <= 10:
        # avg = ((A * 3.5)+(B * 7.5)) / (3.5 + 7.5)
        avg = ((A * 3.5)+(B * 7.5)) / 11
        print(f"Your average: {avg:.5f}")
    else:
        print("ERROR: Grades goes from 0 to 10")


avgGradesWeight()