actual_price = float(input("Enter the actual price: "))
sale_price = float(input("Enter the sale price: "))
if sale_price> actual_price:
    amount= sale_price - actual_price
    print("The total profit is:", amount)
else:
    amount= actual_price - sale_price
    print("The total loss is:", amount)