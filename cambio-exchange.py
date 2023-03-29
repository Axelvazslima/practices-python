# Program that converts between R$ (Brazil) and U$ (US)

def moneyConversor():
    reais = float(
        input("Tell us how much R$ you got and we will trade it to U$ Dollars: "))
    dollars = eval(f"{reais / 5.5}")
    print(
        f"We have a dollar as R$5.5 as parameter, you have R${reais} but just {dollars}U$\n")

moneyConversor()