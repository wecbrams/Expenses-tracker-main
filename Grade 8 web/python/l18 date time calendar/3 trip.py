import random

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Lagos":
        return 300
    elif city == "Abuja":
        return 250
    elif city == "Nairobi":
        return 350
    elif city == "Mombasa":
        return 320
    else:
        return 0  

def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


# Cities from Nigeria and Kenya
cities = ["Lagos", "Abuja", "Nairobi", "Mombasa"]

# Randomly choose a city
selected_city = random.choice(cities)

print("Selected city:", selected_city)
print("Total trip cost:", trip_cost(selected_city, 7, 500))