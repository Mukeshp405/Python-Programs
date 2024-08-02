# Accept price and quantity from user

price = int(input("Enter the price :- "))
quantity = int(input("Enter the quantity :- "))

# calculate total amount
amount = price * quantity

if(amount > 2000):
    print("15%, discount is applicable")
    discount = amount * (15 / 100)
    amount = amount - discount

# Statement print after if condition is True as well as False
print("Amount payable :- ", amount)