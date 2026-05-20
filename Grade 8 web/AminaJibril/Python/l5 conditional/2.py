actual_cost=float(input("Enter the actual product price: "))
sale_amount=float(input("Enter the Sale price: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print(f"The Profit = {amount}")
else:
    amount = actual_cost - sale_amount
    print(f"The Loss = {amount}")
