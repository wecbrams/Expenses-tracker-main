class Parrot:  
    # class attribute (shared by all parrots)
    species = "bird"

    # constructor (instance attributes)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return self.name + " sings " + song

    def dance(self):
        return self.name + " is dancing"

# create objects
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access class attribute
print(blu.name, "is a", blu.species)
print(woo.name, "is a", woo.species)

# access instance attributes
print(blu.name, "is", blu.age, "years old")
print(woo.name, "is", woo.age, "years old")

# call methods
print(blu.sing("Happy"))
print(woo.dance())
