# Hotel Cost
def hotel_cost(nights):
    return 140 * nights
# Plane Ride Cost
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
# Rental Car Cost
def rental_car_cost(days):
    if days >= 7:
        return (40 * days) - 50
    elif days >= 3:
        return (40 * days) - 20
    else:
        return 40 * days
# Total Trip Cost
def trip_cost(city, days, spending_money):
    return (
        hotel_cost(days)
        + plane_ride_cost(city)
        + rental_car_cost(days)
        + spending_money
    )
# Display Results
print("Car Rental Cost:",
      rental_car_cost(5))
print("Plane Cost:",
      plane_ride_cost("Los Angeles"))
print("Hotel Cost:",
      hotel_cost(7))
print("Total Trip Cost:",
      trip_cost("Los Angeles", 7, 500))
print("Total Tampa Trip Cost:",
      trip_cost("Tampa", 6, 500))