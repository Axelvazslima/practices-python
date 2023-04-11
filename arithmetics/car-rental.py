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