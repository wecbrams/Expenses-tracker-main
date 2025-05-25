def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return sum(digit**power for digit in digits) == number

n = 500  # Testing
armstrong_numbers = [num for num in range(n) if is_armstrong(num)]
print(f"Armstrong numbers up to {n}: {armstrong_numbers}")
