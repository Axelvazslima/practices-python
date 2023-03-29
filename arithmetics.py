# Working with numbers

# Program that reads an input number and gives it's antecessor and sucessor, it's double, triple and square root values
baseNum = int(input("Pick a number to get it's informations: "))
# Instead of baseNum**(1/2) it can be pow(baseNum, (1/2)) or using the Math library
print(f"""
You picked {baseNum}
It's antecessor is {baseNum - 1}
It's sucessor is {baseNum + 1}
It's square root value: {baseNum**(1/2)}
It's double: {baseNum * 2}
It's triple: {baseNum * 3}
""")

# Pick a student grades and show it's average values
print("Put your grades and we calculate your average")
firstGrade = input("First grade: ")
secondGrade = input("Second grade: ")
averageGrades = print((float(firstGrade) + float(secondGrade)) / 2, "\n")

# Write a code to convert a mesure from m to cm and mm


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

# Calculator API with Basic operators


def calculator():
    operators = ['*', '**', '+', '/', '//', '%', '-']
    print(f"""
Calculator time!
Your available operators are {operators}     
""")
    num1 = float(input('Number: '))
    operator = input('Operator sign: ')
    num2 = float(input('Another Number: '))
    if operator in operators:
        result = eval(f"{num1}{operator}{num2}")
        print(f"{num1} {operator} {num2} = {result} \n")
    else:
        print(f"Pick an operator from this list: {operators} and try again.")
        operatorAgain = input("Try again with a valid operator sign: ")
        if operatorAgain in operators:
            resultNew = eval(f"{num1}{operatorAgain}{num2}")
            print(f"{num1} {operatorAgain} {num2} = {resultNew}")
        else:
            print("Alright, I give up. \n")


calculator()

# Number table using a for loop


def table():
    tableNumber = float(input(
        "Pick a number and we give you it's multiplication table from 0 to your desired number: "))
    desiredStop = int(input("Stop point: "))
    for i in range(desiredStop + 1):
        # It can use the result var and eval function as well like a did previously but I wanted this one to be different
        # resultTable = eval(f"{tableNumber * i}")
        # print(f"{tableNumber} * {i} = {resultTable}")
        print(f"{tableNumber} * {i} = {tableNumber * i}")
    print("\n")


table()

# Program that converts between R$ (Brazil) and U$ (US)


def moneyConversor():
    reais = float(
        input("Tell us how much R$ you got and we will trade it to U$ Dollars: "))
    dollars = eval(f"{reais / 5.5}")
    print(
        f"We have a dollar as R$5.5 as parameter, you have R${reais} but just {dollars}U$\n")


moneyConversor()

# A program that calculates the area of a wall getting it's height and width. Then say how much tint you need to paint it (A tint litter paints 2 m²)


def wallArea():
    height = float(input("Wall's height: "))
    width = float(input("Wall's width: "))
    area = height * width
    littersTint = area / 2
    print(f"A {height}m tall and {width}m wide wall has an area of {area}m. Each litter of paint can paint 2m² of area. So you will need {littersTint}l of tint to fully paint it")


wallArea()

# Program that reads a discount and adds it to the product value


def discounter():
    productPrice = float(input("FOR THE CASHIER >> Input product price: "))
    discountValue = int(input("FOR THE CASHIER >> Input discount %: "))
    productName = input("What are you buying? ")
    discount = productPrice - (productPrice * (discountValue / 100))
    change = float(
        input("FOR THE CASHIER >> How much is the client paying? ")) - discount
    if change >= 0:
        print(f"You are a buying a {productName}. It costs {productPrice}$ but you have {discountValue}$% of discount. Your total now is {discount:.2f}$ and your change is {change:.2f}$")
    else:
        print("Insufficient funds.")


discounter()

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

# Temperature conversor


def temperatureConversor():
    celsius = ["ºC", "C", "CELSIUS", "Cº"]
    fahrenheit = ["ºF", "F", "FAHRENHEIT", "Fº"]
    kelvin = ["KELVIN", "K"]
    scale = input("What scale are you using? ")
    temp = float(input("How hot is there? "))
    if scale.upper() in celsius:
        c = temp
        f = (c * 1.8) + 32
        k = c + 273.15
        print(f"Your temperature is {c}ºC, so it's {f}ºF and {k}K")
    if scale.upper() in fahrenheit:
        f = temp
        c = (f - 32)/(9/5)
        k = (f+459.67) * 5/9
        print(f"Your temperature is {f}ºF, so it's {c}ºC and {k}K")
    if scale.upper() in kelvin:
        k = temp
        c = k-273.15
        f = (((k-273.15)*9)/5)+32
        print(f"Your temperature is {k}K, so it's {c}ºC and {f}ºF")


temperatureConversor()

# Calculating a Area


def circleArea():
    print("Give me a circle radius and receive it's area back")
    n = 3.14159
    R = round(float(input("(TWO DECIMAL HOUSES) Radius: ")), 2)
    A = n * R**2
    print(f"A={A}")


circleArea()

# Average grades with A's weight = 3.5 and B's weight = 7.5


def avgGradesWeight():
    A = round(float(input("First grade: ")), 1)
    B = round(float(input("Second grade: ")), 1)
    if A <= 10 and B <= 10:
        # avg = ((A * 3.5)+(B * 7.5)) / (3.5 + 7.5)
        avg = ((A * 3.5)+(B * 7.5)) / 11
        print(f"Your average: {avg:.5f}")
    else:
        print("ERROR: Grades goes from 0 to 10")


avgGradesWeight()

# Calculate average grades with 3 grades and it's weights


def calcAvgThreeGrades():
    print("Input your grades and we give you your average. A has weight 2, B has weight 3 and C has weight 5.")
    A = round(float(input("First grade: ")), 1)
    B = round(float(input("Second grade: ")), 1)
    C = round(float(input("Third grade: ")), 1)
    if A <= 10 and B <= 10 and C <= 10:
        avg = (A*2 + B*3 + C*5) / 10
        print(f"Your average is {avg}")
    else:
        print("MAX GRADE IS 10.")


calcAvgThreeGrades()

# Getting the Max value between 3 values


def maxValue():
    print("Give us three numbers and we return you the greatest one")
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    biggerAb = (a+b+abs(a-b))/2
    greatest = (biggerAb + c + abs(biggerAb - c))/2
    print(f"{greatest} is the greatest.")


maxValue()

# Rent a car. R$60 a day and R$0.15 per KM


def carRental():
    print("Calculate your car rent if > R$0.15 per KM and R$60 a day")
    initialKm = int(input("Initial KM of the car: "))
    km = int(input("KM after you using it: "))
    totalKm = km - initialKm
    days = int(input("Number of days you used the car: "))
    price = totalKm * 0.15 + days * 60
    print(f"You used the car for {days} days, riding it from {initialKm} to {km}; a total of {totalKm}. Each KM costs R$0.15 and each day costs R$60, so your total is R${price:.2f}")


carRental()

# Calculating the salary for an employee based on his work hours


def salaryPerHour():
    number = int(input())
    workedHours = int(input())
    perHour = float(input())
    salary = workedHours * perHour
    print(f"""NUMBER = {number}
    SALARY = U$ {salary:.2f}""")


salaryPerHour()

# Tell how many notes you will get back if you want to trade your money for smaller and equal notes


def bankNotesCalc():
    print("How many notes you can get back if you decide to trade your note to smaller and equal notes notes")
    value = int(input("Money: "))
    if value > 0 and value < 1000000:
        bankNotes = [100, 50, 20, 10, 5, 2, 1]
        print(value)
        for i in range(len(bankNotes)):
            division = value // bankNotes[i]
            print(f"{division} nota(s) de {bankNotes[i]}")


bankNotesCalc()


def bankNotesCalcExtra():
    print("We calculate how many notes you will get back if you decide to trade a note")
    money = int(input("Money: "))
    if money > 0 and money < 1000000:
        notes = [100, 50, 20, 10, 5, 2, 1]
        print(money)
        for i in range(len(notes)):
            division = money // notes[i]
            money = money - (division * notes[i])
            print(f"{division} nota(s) de {notes[i]}")


bankNotesCalcExtra()

# Salary Comission Calculator


def salaryBonus():
    sellersName = input("Your name: ").upper()
    salary = float(input("Your salary: "))
    sales = float(
        input("(JUST THE NUMBER and use '.' not ',') Your total sales in R$: "))

    total = (sales * 0.15) + salary

    print(f"{sellersName}, your total salary is R$ {total}")


salaryBonus()


def baskhara():
    values = input().split()
    line = [float(i) for i in values]
    a = line[0]
    b = line[1]
    c = line[2]
    delta = (b**2) - (4*a*c)

    if 2*a == 0 or delta < 0:
        print("Impossivel calcular")
    else:
        xI = (-b + delta**(1/2))/(2*a)
        xII = (-b - delta**(1/2))/(2*a)
        print(f"""R1 = {xI:.5f}
    R2 = {xII:.5f}""")


baskhara()

# Salary Calculator


def salaryCalculatorMutableBonus():
    salary = round(float(input()), 2)
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

# Printing the even numbers in a range defined by the user


def evenNumbersX():
    wantedNumber = int(input())
    for i in range(wantedNumber + 1):
        if i % 2 == 0:
            print(f"{i}")


evenNumbersX()

# Telling if a number is odd or even or null(0) + if it's positive or negative


def tellerEvenOdd():
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


def gpdVal():
    print("Input two GPD variations -> negative is decrease, positive is increase. The programm will convert it into percentages, dont worry about it")
    gdpVar = input("Variation of GDP: ").split()
    gdp = [round(float(i), 2) for i in gdpVar]
    F1 = gdp[0]
    F2 = gdp[1]
    calc = ((1 + F1/100) * (1 + F2/100) - 1) * 100
    print(f"{calc:.6f}")


gpdVal()


def positiveNumbersPrinter():
    print("Write us 6 numbers and we will tell you how many of them are positives")
    everyN = [float(input("Enter 6 numbers (1 at a time): ")),
              float(input()),
              float(input()),
              float(input()),
              float(input()),
              float(input())]
    positives = []
    for i in everyN:
        if i > 0:
            positives.append(i)
    print(f"{len(positives)} valores positivos")


positiveNumbersPrinter()

# Password checker loop


def passwordChecker():
    password = int(input("Enter password: "))
    while password != 2002:
        print("Senha Invalida")
        password = int(input())
    if password == 2002:
        print("Acesso Permitido")


passwordChecker()

# Finding the middle value in an array


def findMiddleValue():
    print("""We are finding the middle value in the numbers you put in.

    Instructions: 
    1- Enter a number
    2- hit space then put another number (Do this until you are good.)
    3- When you are done hit enter.""")
    agesInput = input("Input numbers: ").split()
    ages = [int(i) for i in agesInput]
    ages.sort()
    iMiddle = len(ages)//2
    if len(ages) % 2 == 0:
        middle = (ages[(iMiddle) - 1] + ages[iMiddle]) / 2
    else:
        middle = ages[iMiddle]
    print(middle)
