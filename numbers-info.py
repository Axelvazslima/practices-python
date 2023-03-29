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