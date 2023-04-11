# Calculating the salary for an employee based on his work hours

def salaryPerHour():
    print("""Calculating an employee salary based off his work hours.
For this operation we need the employee's number (ID), his worked hours and how much he makes an hour.""")
    name = input("Employee's name: ")
    number = int(input("Employee's ID: "))
    workedHours = int(input(f"{name} worked hours:"))
    perHour = float(input(f"{name}'s U$ per hour: "))
    salary = workedHours * perHour
    print(f"(ID: {number}) {name}'s salary: U${salary:.2f}")

salaryPerHour()