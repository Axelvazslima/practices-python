money = round(float(input()), 2)

notes = [100, 50, 20, 10, 5, 2]

print("Money notes:")
for i in range(len(notes)):
    quantity_notes = money // notes[i]
    money = money - (notes[i] * quantity_notes)
    print(f"{quantity_notes:.0f} U${notes[i]:.2f}")

coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("Coins:")
for j in range(len(coins)):
    quantity_coins = money // coins[j]
    money = money - (coins[j] * quantity_coins)
    print(f"{quantity_coins:.0f} U${coins[j]:.2f}")
