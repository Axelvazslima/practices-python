# Tell how many notes you will get back if you want to trade your money for smaller and equal notes

def bankNotesCalc():
    print("How many notes you can get back if you decide to trade your money for smaller and equal notes")
    value = int(input("Money: "))
    if value > 0 and value < 1000000:
        bankNotes = [100, 50, 20, 10, 5, 2, 1]
        print(value)
        for i in range(len(bankNotes)):
            division = value // bankNotes[i]
            print(f"{division} nota(s) de {bankNotes[i]}")

bankNotesCalc()