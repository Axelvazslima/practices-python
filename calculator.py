# Calculator API for basic operators

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