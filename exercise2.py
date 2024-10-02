# Write a python program to check a list contain even number or odd number.

def check_even_odd(numbers):
    has_even = any(num % 2 == 0 for num in numbers)
    has_odd = any(num % 2 != 0 for num in numbers)

    if has_even and has_odd:
        print("The list contains both even and odd numbers.")
    elif has_even:
        print("The list contains only even numbers.")
    elif has_odd:
        print("The list contains only odd numbers.")
    else:
        print("The list contains no numbers.")

# Example usage
numbers = [1, 3, 5, 7, 9]  # Change this list to test different cases
check_even_odd(numbers)
