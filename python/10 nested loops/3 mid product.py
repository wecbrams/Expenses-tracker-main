# Input a number
num = input("Enter the number: ")

# Check if number has 4 or more digits
if len(num) >= 4:
    mid1_index = len(num) \\ 2 - 1
    mid2_index = mid1_index + 1

    # Get middle digits
    midOne = int(num[mid1_index])
    midTwo = int(num[mid2_index])

    # Calculate product
    product = midOne * midTwo

    # Display result
    print(f"\nProduct of Mid digits ({midOne} * {midTwo}) = {product}")
else:
    print("\nIt's not a 4 or more digit number!")
