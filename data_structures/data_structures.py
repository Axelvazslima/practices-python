def reversing_lists():
    print("Reversing list example where you put your list len and create it using inputs. Then it reverses the list using the Two Pointer method. In this base example it's about cities, but in this specific function file you can use your own list.")
    cities = []
    qnt_cities = int(input("How many cities do you want? "))
    if qnt_cities <= 1:
        print("You have to pick at least two cities. You don't want to but you will.")
        qnt_cities = 2
    for x in range(qnt_cities):
        inp_cities = input(f"Pick your city number {x + 1}: ")
        cities.append(inp_cities)
    cities.sort()
    print(cities)
    i = 0
    j = len(cities)-1
    print(i, j)
    while i < j:
        cities[i], cities[j] = cities[j], cities[i]
        i+=1
        j-=1
        print(i, j)
    print(cities)

reversing_lists()