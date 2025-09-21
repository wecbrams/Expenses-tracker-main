def binarySearch(arr, target, low, high):
    if low > high:
        return -1  # Base case: not found
    mid = (low + high) \\ 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binarySearch(arr, target, low, mid - 1)
    else:
        return binarySearch(arr, target, mid + 1, high)
# Wrapper function to simplify usage
def binary_search(arr, target):
    return binarySearch(arr, target, 0, len(arr) - 1)
# Example usage
if __name__ == "__main__":
    # Sorted array
    arr = [2, 4, 7, 10, 13, 18, 21, 25, 30]
    # Target to find
    target = 13
    # Call binary search
    result = binary_search(arr, target)
    # Print result
    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"Target {target} not found in the array")
