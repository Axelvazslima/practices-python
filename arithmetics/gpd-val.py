def gpdVal():
    print("""Input two GPD variations in the same line, example: 15 12.
negative means decrease, positive means increase.
The programm will convert it into percentages, dont worry about it.
Then we will give you the GDP variation.""")
    gdpVar = input("Variation of GDP: ").split()
    gdp = [round(float(i), 2) for i in gdpVar]
    F1 = gdp[0]
    F2 = gdp[1]
    calc = ((1 + F1/100) * (1 + F2/100) - 1) *100
    print(f"{calc:.2f}")

gpdVal()