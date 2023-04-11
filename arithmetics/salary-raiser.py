# Program to give an employee a raise

def salaryRaiser():
    salary = int(input('Your salary: '))
    salaryRaise = int(input("Salary raise %: "))
    newSalary = eval(f"{salary} * 1.{salaryRaise}")
    tax = int(input('Tax %: '))
    afterTax = newSalary-(newSalary * (tax/100))
    print(
        f"Your base salary was {salary}, but you earned a {salaryRaise}% raise and now it's in {newSalary}. Your state tax is {tax}%, so your real salary is {afterTax}")

salaryRaiser()