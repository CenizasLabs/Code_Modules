# REQUIREMENTS
import math

# FUNCTIONS
def compute_gcd(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute GCD.")
    
    gcd_result = numbers[0]
    
    for i in range(1, len(numbers)):
        gcd_result = math.gcd(gcd_result, numbers[i])
    
    return gcd_result

# EXAMPLE USAGE
numbers = [12, 18, 24]
result = compute_gcd(numbers)
print(f"The GCD of {numbers} is {result}")