# Money exchange to smaller notes

def bankNotesCalcExtra():
    print("We calculate how many notes you will get back if you decide to trade your money note.")
    money = int(input("Money: "))
    if money > 0 and money < 1000000:
        notes = [100, 50, 20, 10, 5, 2, 1]
        print(money)
        for i in range(len(notes)):
            division = money // notes[i]
            money = money - (division * notes[i])
            print(f"{division} nota(s) de {notes[i]}")


bankNotesCalcExtra()