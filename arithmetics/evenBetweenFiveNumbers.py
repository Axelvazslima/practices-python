print("""Input five numbers (int > enter > 5 times) then the code will tell you how many of this 5 numbers are even""")
values = [int(input()) for i in range(5)]
even = 0
for j in values:
    if j % 2 == 0:
        even += 1
print(f"{even} valores pares")