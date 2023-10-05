# REQUIREMENTS
import math

# FUNCTIONS
def compute_lcm(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute LCM.")
    
    lcm_result = numbers[0]
    
    for i in range(1, len(numbers)):
        lcm_result = math.lcm(lcm_result, numbers[i])
    
    return lcm_result

# EXAMPLE USAGE
numbers = [12, 18, 24]
result = compute_lcm(numbers)
print(f"The LCM of {numbers} is {result}")
