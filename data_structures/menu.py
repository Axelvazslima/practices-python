def menu():
    product_info = {
        1: ['Pepperoni', 35],
        2: ['Shrimp', 50],
        3: ['Chocolate', 40],
        4: ['Mozzarella', 20],
        5: ['Margherita', 48]
    }
    return product_info


def menu_view():
    product_info = menu()
    print(f"\n{'Pizzas':^35}")
    print(f"|{'Code':>5}|{'Name':^20}|{'Price':>5}|")
    for i in range(1, 6):
        print(
            f"|{i:>5}|{product_info[i][0]:>20}|{product_info[i][1]:>5}|"
        )
    print(f'\n')



def total():
    print('If you input anything besides the numbers that matchs the requirements we close your order.')
    total = 0
    while True:
        product = input("Input your product code: ")
        try:
            product = int(product)
            quantity = int(input("How many of these are you buying? "))
        except:
            return total
        cur_product = menu()[product]
        total += cur_product[1] * quantity


def main():
    menu_view()
    print("This code calculates your total getting your product code and it's quantity. All informations in the menu above.")
    print(f'Your total is: {total():.2f} U$')


main()
