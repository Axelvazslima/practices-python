# Salary Comission Calculator

def salaryBonus():
    print("We calculate your comission (usually bonus off sales) and your final total salary using your sales number and your base salary.\nAlways put just the number")
    sellersName = input("Your name: ").upper()
    salary = float(input("Your salary: "))
    sales = float(
        input("(Use '.' instead of ',' for decimals) Your total sales in U$: "))
    bonusPerSale = float(input("Your company bonus for sale: "))
    tax = float(input("The total tax you have to pay (absolute value, like: 15% = 15): "))/100
    total = (sales * bonusPerSale) + salary
    liquid = total*tax
    print(f"{sellersName}, your total salary is U$ {total}.\nAfter tax you get: {liquid}")

salaryBonus()