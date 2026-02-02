units = int(input("Enter number of units consumed: "))
if units < 50:
    amount = units * 2.5
    surcharge = 25
elif units < 150:
    amount = units * 5.0
    surcharge = 50
elif units < 250:
    amount = units * 6.0
    surcharge = 75
else:
    amount = (50 * 2.5) + (100 * 5.0) + (100 * 6.0) + (units - 250) * 7.5
    surcharge = 100
total= amount + surcharge
print(f"Electricity Bill: {total} (Amount: {amount} + Surcharge: {surcharge})")