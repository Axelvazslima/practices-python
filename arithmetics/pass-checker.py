def passwordChecker():
    password = int(input("Enter password: "))
    while password != 2002:
        print("Senha Invalida")
        password = int(input())
    if password == 2002:
        print("Acesso Permitido")


passwordChecker()