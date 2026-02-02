num = 3
if num > 0:
    print(num, "is a positive number")

num = -3
if num > 0:
    print(num, "is a positive number")


# Profit Loss
actual_price=float(input("Enter the actual price: "))
sale_amount = float(input("Enter the sales amount: "))

if (sale_amount > actual_price):
    amount = sale_amount - actual_price
    print(f"Total profit = {amount}")

else:
    amount=actual_price -sale_amount
    print(f"Total loss = {amount}")

