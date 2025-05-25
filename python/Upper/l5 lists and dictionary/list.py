# Initialize the list
lst = ["Apple", "Guava", "Mango", "Banana", "Kiwi"]
# Print length of list
print("Length of list:", len(lst))
# Print first and last elements
print("First Element:", lst[0])
print("Last Element:", lst[-1])
# Append 'Papaya' to the list
lst.append('Papaya') #add
print("Updated List:", lst)
# Remove 'Guava' from the list
lst.remove('Guava')
print("Updated List after removing 'Guava':", lst)
# Sort the list
lst.sort()
print("Sorted List:", lst)
# Pop the element at index 1
lst.pop(1)
print("Updated List after popping index 1:", lst)
# Reverse the list
lst.reverse()
print("Reversed List:", lst)
# Demonstrate list multiplication
print("Multiplication on List:", lst * 2)
# Slicing the first 4 elements
print("Sliced List (first 4 items):", lst[:4])
# Clear the list
lst.clear()
print("Updated List after clearing:", lst)
