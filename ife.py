actual_cost= float(input("Please Enter the actual produc price: "))
sale_amount= float(input("Enter the sale amount"))
if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = {0}".format(amount))
else:
    print("No profit")