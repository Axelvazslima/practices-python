def salaryCalculatorMutableBonus():
    print("Everyone will get a raise! The increase is going to be inversely proportional to your present salary. Just input your salary and we give you the new one.")
    salary = round(float(input("Your salary: ")), 2)
    perCent = [1.15, 1.12, 1.1, 1.07, 1.04]
    if salary > 0:
        if salary <= 400:
            newSalary = salary * perCent[0]
            newPerCent = 0.15 * 100
        elif salary > 400 and salary <= 800:
            newSalary = salary * perCent[1]
            newPerCent = (perCent[1]-1.0) * 100
        elif salary > 800 and salary <= 1200:
            newSalary = salary * perCent[2]
            newPerCent = (perCent[2]-1.0) * 100
        elif salary > 1200 and salary <= 2000:
            newSalary = salary * perCent[3]
            newPerCent = (perCent[3]-1.0) * 100
        elif salary > 2000:
            newSalary = salary * perCent[4]
            newPerCent = (perCent[4]-1.0) * 100
        print(f"""Novo salario: {newSalary:.2f}
    Reajuste ganho: {newSalary - salary:.2f}
    Em percentual: {int(newPerCent)} %""")


salaryCalculatorMutableBonus()