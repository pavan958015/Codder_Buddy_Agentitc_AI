import math

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers (a - b)."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers (a / b). Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Returns base raised to the power of the exponent."""
    return math.pow(base, exponent)

def square_root(number):
    """Returns the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(number)

def sine(angle_radians):
    """Returns the sine of an angle in radians."""
    return math.sin(angle_radians)

def cosine(angle_radians):
    """Returns the cosine of an angle in radians."""
    return math.cos(angle_radians)

def tangent(angle_radians):
    """Returns the tangent of an angle in radians."""
    # Handle potential division by zero near pi/2 or 3pi/2, though math.tan handles it via float limits
    return math.tan(angle_radians)

def logarithm(number, base=math.e):
    """
    Returns the logarithm of a number to a given base.
    If no base is provided, it defaults to natural logarithm (base e).
    Raises ValueError if number <= 0.
    """
    if number <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(number, base)

# Example usage (optional, for testing purposes):
if __name__ == '__main__':
    print(f"Addition of 5 and 3: {add(5, 3)}")
    print(f"Division of 10 by 2: {divide(10, 2)}")
    print(f"Square root of 81: {square_root(81)}")
    print(f"Sine of pi/2 (approx): {sine(math.pi / 2)}")
    try:
        print(f"Logarithm of 10 with base 10: {logarithm(10, 10)}")
    except ValueError as e:
        print(f"Error in log test: {e}")