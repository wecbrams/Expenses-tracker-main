a=5
b=2.5
c="codigal"
d=True
print("Data type of a", type(a))
print("Data type of b", type(b))
print("Data type of c", type(c))
print("Data type of d", type(d))

# Type Casting
print('\nAfter type casting')
a =str(a)
b=int(b)
print("Data type of a and it's value is", type(a),a)
print("Data type of b it's value is", type(b),b)


# Input Words
text=input("Enter a word: ")

# reverse
rev=text[::-1]
print("Reversed word is:\n",rev)