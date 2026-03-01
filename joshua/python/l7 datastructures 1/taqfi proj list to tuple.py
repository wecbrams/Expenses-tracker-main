# Creating a tuple and a list
lst = [2, 3.5, "orange", "mango", "jackfruit", True, False]

# Turning tuple to list and doing operations on it
tp = tuple(lst)

tolist = list(tp)
print(f"Tuple to List: {tp} \n")
print("Operations on the converted Tuple to List \n")

tolist.append("cheese")
print(f"List after adding an item: {tp} \n")

tolist.pop(5)
print(f"List after removing a specific item: {tp} \n")

print(f"Final Updated List: {tp} \n")