actual_cost= float(input("Enter the Actual price: "))
Sale_cost= float(input("Enter the Sales price: "))

if Sale_cost > actual_cost:
    amount = Sale_cost - actual_cost
    print(f"Total profit = {amount}")
else:
    amount = Sale_cost - actual_cost
    print(f"Ooops!!!\nTotal Loss = {amount}")