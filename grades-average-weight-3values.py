# Calculate average grades with 3 grades and it's weights

def calcAvgThreeGrades():
    print("""Input your grades and we give you your average. 
First grade has weight 2. Second grade has weight 3. Third grade has weight 5.""")
    A = round(float(input("First grade: ")), 1)
    B = round(float(input("Second grade: ")), 1)
    C = round(float(input("Third grade: ")), 1)
    if A <= 10 and B <= 10 and C <= 10:
        avg = (A*2 + B*3 + C*5) / 10
        print(f"Your average is {avg}")
    else:
        print("MAX GRADE IS 10.")

calcAvgThreeGrades()