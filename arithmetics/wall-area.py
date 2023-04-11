# A program that calculates the area of a wall getting it's height and width. Then say how much tint you need to paint it (A tint litter paints 2 m²)

def wallArea():
    height = float(input("Wall's height: "))
    width = float(input("Wall's width: "))
    area = height * width
    littersTint = area / 2
    print(f"A {height}m tall and {width}m wide wall has an area of {area}m. Each litter of paint can paint 2m² of area. So you will need {littersTint}l of tint to fully paint it")

wallArea()