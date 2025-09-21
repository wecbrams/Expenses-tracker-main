class Computer:
    def __init__(self):
        self.__maxprice = 900  # Note the underscore: this indicates a "protected" variable by convention

    def sell(self):
        print("Selling Price: ",self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price

# Create object
c = Computer()
c.sell() # shows 900

# Try changing the price directly
c.__maxprice = 1000
c.sell() # Shows 900

# Using setter function
c.setMaxPrice(1000)
c.sell() #Shows 1000