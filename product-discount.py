# Program that reads a discount and adds it to the product value

def discounter():
    productPrice = float(input("FOR THE CASHIER >> Input product price: "))
    discountValue = int(input("FOR THE CASHIER >> Input discount %: "))
    productName = input("What are you buying? ")
    discount = productPrice - (productPrice * (discountValue / 100))
    change = float(
        input("FOR THE CASHIER >> How much is the client paying? ")) - discount
    if change >= 0:
        print(f"You are a buying a {productName}. It costs {productPrice}$ but you have {discountValue}$% of discount. Your total now is {discount:.2f}$ and your change is {change:.2f}$")
    else:
        print("Insufficient funds.")

discounter()